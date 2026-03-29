# Binance Futures Testnet Trading Bot

## Overview
This is a simple Python-based trading bot that places MARKET and LIMIT orders on Binance Futures Testnet.

## Features
- Place BUY and SELL orders
- Supports MARKET and LIMIT orders
- CLI-based input
- Logging of requests and responses
- Error handling and validation

## Project Structure

```
trading_bot/
│
├── bot/
│   ├── client.py          # Handles Binance API connection
│   ├── orders.py          # Order placement logic
│   ├── validators.py      # Input validation
│   └── logging_config.py  # Logging setup
│
|
|
├── cli.py                 # Main entry point (user interaction)
├── requirements.txt       # Dependencies
├── README.md              # Project documentation
├── .gitignore             # Ignore sensitive files
└── trading_bot.log        # Log file (generated after running)

## Author
Yash Nibe
