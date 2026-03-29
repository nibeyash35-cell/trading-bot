import os
from binance.client import Client
from dotenv import load_dotenv

def get_client():
    load_dotenv()

    api_key = os.getenv("BINANCE_API_KEY")
    secret_key = os.getenv("BINANCE_SECRET_KEY")

    client = Client(api_key, secret_key)
    client.FUTURES_URL = "https://testnet.binancefuture.com/fapi"

    return client