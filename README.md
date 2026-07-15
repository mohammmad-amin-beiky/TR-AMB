# TR-AMB
Core ML framework for algorithmic trading bots. A lightweight demo of self-learning models using Binance data, built for the TR-AMB ecosystem.
# TR-AMB Quant Core: Machine Learning Trading Bot (Simple Demo)

## About the Founder & Company
**Author:** Mohammad Amin Beiki (Founder & Lead Architect at TR-AMB)

- **Python Developer (ML Specialist):** 3 years of experience in designing scalable machine learning pipelines.
- **Financial Market Analyst:** 3 years of deep analysis in Forex and Crypto markets.
- **Active Trader:** Practical experience in algorithmic and manual trading strategies.
- **Company:** Founder and Lead Architect of **TR-AMB**.
- **Current Project:** Overseeing the architecture and production of over 50 self-learning AI trading bots and analytical tools.

## Project Overview
This repository contains a **super simple, minimalistic demo** of our core architecture. 
Although this specific script is kept intentionally lightweight and linear for demonstration purposes, **it represents the fundamental logic layer** used within our proprietary ecosystem.

### The Full-Scale Architecture (Not Shown Here)
In our actual production environment (which powers our Android & iOS applications), this exact logic is wrapped in:

- **Modular OOP structures** for scalability.
- **Real-time WebSocket data streaming** (instead of basic REST calls).
- **Advanced Feature Engineering** and ensemble ML models.
- **Mobile API integration** (FastAPI/Django) to serve predictions directly to the TR-AMB mobile apps.

## Features of this Demo Bot
This simple Python script demonstrates our core data flow:

- **Live Data Fetching:** Pulls the last 100 1-hour candles for 4 major cryptocurrencies (BTC, ETH, BNB, SOL) directly from the Binance public API.
- **Automated Feature Engineering:** Automatically calculates technical indicators (returns, volume moving averages).
- **Self-Learning ML Model:** Utilizes `scikit-learn` (Random Forest Classifier) to train itself on the last 100 candles and predict the immediate future trend (Long/Short) without manual parameter tuning.
- **Visualization:** Generates a comprehensive 2x2 matplotlib chart showing the price action of all 4 assets.
- **GUI Integration:** Features a functional `Tkinter` dashboard to easily trigger the analysis.

## Installation
To run this demo, install the required dependencies:

```bash
pip install requests pandas numpy scikit-learn matplotlib
