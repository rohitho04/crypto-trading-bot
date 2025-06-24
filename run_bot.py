from dotenv import load_dotenv
import os

load_dotenv()

api_key = os.getenv("API_KEY")
api_secret = os.getenv("API_SECRET")

import logging
import os

# ✅ Ensure logs folder exists
if not os.path.exists("logs"):
    os.makedirs("logs")

# ✅ Configure logging
logging.basicConfig(
    filename='logs/bot.log',
    level=logging.INFO,
    format='%(asctime)s %(levelname)s:%(message)s'
)

from trading_bot import BasicBot

def main():
    print("=== Binance Futures Bot ===")
    # Pre-filled testnet API keys
    api_key = "4d71a0bf8e6f644e12ae050d3cc70b147b0fdbed14d6759d69e3b94e9e90505b"
    api_secret = "4f15d6781b1b95a3c6430248760caec69ebf5897874b58d21f4948101190b660"

    bot = BasicBot(api_key, api_secret)

    symbol = input("Symbol (e.g. BTCUSDT): ").upper()
    side = input("Side (buy/sell): ").lower()
    order_type = input("Order Type (MARKET / LIMIT): ").upper()
    quantity = float(input("Quantity: "))
    price = None

    if order_type == "LIMIT":
        price = float(input("Enter Limit Price: "))

    bot.place_order(symbol, side, order_type, quantity, price)

if __name__ == "__main__":
    main()
    
