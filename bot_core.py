import requests
import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt
from tkinter import Tk, Label, Button, Text, Scrollbar, END
import threading

symbols = ['BTCUSDT', 'ETHUSDT', 'BNBUSDT', 'SOLUSDT']

def fetch_data():
    data_list = []
    for sym in symbols:
        url = f"https://api.binance.com/api/v3/klines?symbol={sym}&interval=1h&limit=100"
        res = requests.get(url).json()
        df = pd.DataFrame(res, columns=['time', 'open', 'high', 'low', 'close', 'volume', 'ct', 'cav', 'tn', 'tb', 'tv', 'ti'])
        df['close'] = df['close'].astype(float)
        df['volume'] = df['volume'].astype(float)
        df['sym'] = sym
        data_list.append(df[['sym', 'close', 'volume']])
    return pd.concat(data_list, ignore_index=True)

def analyze_data():
    df = fetch_data()
    results = []
    
    for sym in symbols:
        sub = df[df['sym'] == sym].copy()
        sub['returns'] = sub['close'].pct_change()
        sub['vol_ma'] = sub['volume'].rolling(5).mean()
        sub['target'] = (sub['returns'].shift(-1) > 0).astype(int)
        
        sub = sub.dropna()
        
        X = sub[['returns', 'vol_ma']].values
        y = sub['target'].values
        
        scaler = StandardScaler()
        X_scaled = scaler.fit_transform(X)
        
        model = RandomForestClassifier(n_estimators=10, max_depth=3)
        model.fit(X_scaled, y)
        
        last_X = scaler.transform([X[-1]])
        pred = model.predict(last_X)[0]
        
        results.append(f"{sym}: پیش‌بینی روند بعدی {'صعودی 📈' if pred == 1 else 'نزولی 📉'}")
        
    return df, results

def plot_charts(df):
    fig, axs = plt.subplots(2, 2, figsize=(10, 8))
    fig.suptitle('تحلیل ۱۰۰ کندل یک ساعته (۴ ارز)')
    for i, sym in enumerate(symbols):
        sub = df[df['sym'] == sym]
        row, col = divmod(i, 2)
        axs[row, col].plot(sub['close'].values, label=sym, color='blue')
        axs[row, col].set_title(sym)
        axs[row, col].legend()
    plt.tight_layout()
    plt.show()

def run_analysis():
    output_text.delete(1.0, END)
    output_text.insert(END, "در حال دریافت داده از بایننس...\n")
    try:
        df, analysis_res = analyze_data()
        output_text.insert(END, "تحلیل کامل شد:\n\n")
        for line in analysis_res:
            output_text.insert(END, line + "\n")
        output_text.insert(END, "\nدر حال باز کردن نمودارها...\n")
        plot_charts(df)
    except Exception as e:
        output_text.insert(END, f"خطا: {str(e)}")

def start_thread():
    threading.Thread(target=run_analysis).start()

root = Tk()
root.title("ربات تحلیلی ML")
root.geometry("400x300")

Label(root, text="پنل ربات معاملاتی پایتون", font=("Arial", 12, "bold")).pack(pady=10)
Button(root, text="شروع تحلیل (۱۰۰ کندل)", command=start_thread, bg="green", fg="white").pack(pady=5)

output_text = Text(root, height=10, width=45)
output_text.pack(pady=5)
scroll = Scrollbar(root, command=output_text.yview)
scroll.pack(side="right", fill="y")
output_text.config(yscrollcommand=scroll.set)

root.mainloop()
