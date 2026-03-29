from bot.client import get_client
from bot.orders import place_order
from bot.validators import validate_side, validate_order_type, validate_quantity
from bot.logging_config import setup_logging
import logging

def run():
    print("Program started")

    setup_logging()
    client = get_client()

    try:
        symbol = input("Enter symbol (BTCUSDT): ").upper()
        side = input("Enter side (BUY/SELL): ").upper()
        order_type = input("Enter type (MARKET/LIMIT): ").upper()
        quantity = float(input("Enter quantity: "))

        validate_side(side)
        validate_order_type(order_type)
        validate_quantity(quantity)

        price = None
        if order_type == "LIMIT":
            price = input("Enter price: ")

        logging.info(f"Order Request: {symbol}, {side}, {order_type}, {quantity}, {price}")

        order = place_order(client, symbol, side, order_type, quantity, price)

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


if __name__ == "__main__":
    run()