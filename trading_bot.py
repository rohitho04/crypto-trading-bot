from binance.client import Client
from binance.enums import *
import logging

class BasicBot:
    def __init__(self, api_key, api_secret, testnet=True):
        self.logger = self.setup_logger()
        
        self.client = Client(api_key, api_secret)
        
        if testnet:
            self.client.API_URL = 'https://testnet.binancefuture.com/fapi/v1'  # ✅ MUST BE THIS!
            self.client.FUTURES_URL = 'https://testnet.binancefuture.com/fapi'  # ✅ Also this one
           

        try:
            self.client.futures_account()  # Test connection
            self.logger.info("Connected to Binance Futures Testnet")
        except Exception as e:
            self.logger.error(f"Connection error: {e}")
            print(f"❌ Connection failed: {e}")


    def setup_logger(self):
        logger = logging.getLogger("BotLogger")
        logger.setLevel(logging.INFO)
        handler = logging.FileHandler("bot.log")
        formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
        handler.setFormatter(formatter)
        logger.addHandler(handler)
        return logger

    def place_order(self, symbol, side, order_type, quantity, price=None):
        try:
            params = {
                'symbol': symbol,
                'side': SIDE_BUY if side.lower() == 'buy' else SIDE_SELL,
                'type': order_type,
                'quantity': quantity
            }

            if order_type == ORDER_TYPE_LIMIT:
                params['timeInForce'] = TIME_IN_FORCE_GTC
                params['price'] = price

            order = self.client.futures_create_order(**params)
            self.logger.info(f"Order placed: {order}")
            print("✅ Order placed successfully.")
            return order
        except Exception as e:
            print(f"❌ Error placing order: {e}")
            self.logger.error(f"Order failed: {e}")
            return None
    
