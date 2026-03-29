import os
import logging
from binance.client import Client
from dotenv import load_dotenv

# Logging setup
logging.basicConfig(
    filename="trading_bot.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

print("Program started")

# Load API keys
load_dotenv()

api_key = os.getenv("BINANCE_API_KEY")
secret_key = os.getenv("BINANCE_SECRET_KEY")

# 👇 ADD THESE LINES HERE
print("API KEY START:", api_key[:5] if api_key else None)
print("API KEY END:", api_key[-5:] if api_key else None)

client = Client(api_key, secret_key)
client.FUTURES_URL = "https://testnet.binancefuture.com/fapi"

try:
    symbol = input("Enter symbol (BTCUSDT): ").upper()
    side = input("Enter side (BUY/SELL): ").upper()
    order_type = input("Enter type (MARKET/LIMIT): ").upper()
    quantity = float(input("Enter quantity: "))

    price = None
    if order_type == "LIMIT":
        price = input("Enter price: ")

    # Log request
    logging.info(f"Order Request: {symbol}, {side}, {order_type}, {quantity}, {price}")

    if order_type == "MARKET":
        order = client.futures_create_order(
            symbol=symbol,
            side=side,
            type="MARKET",
            quantity=quantity
        )
    else:
        order = client.futures_create_order(
            symbol=symbol,
            side=side,
            type="LIMIT",
            quantity=quantity,
            price=price,
            timeInForce="GTC"
        )

    # Log response
    logging.info(f"Order Response: {order}")

    print("\n✅ Order Successful")
    print("Order ID:", order.get("orderId"))
    print("Status:", order.get("status"))
    print("Executed Qty:", order.get("executedQty"))
    print("Avg Price:", order.get("avgPrice", "N/A"))

except Exception as e:
    logging.error(str(e))
    print("\n❌ ERROR:", e)

input("\nPress Enter to exit...")