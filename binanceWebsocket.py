import websocket
import json
import time
import Composition
from datetime import datetime
class BinanceWebsocket:
    def __init__(self , pair):
        self.pair=pair
        self.ws = websocket.WebSocketApp("wss://stream.binance.com:9443/ws/{}@depth".format(pair),  
                                         on_message=self.on_message,
                                         on_error=self.on_error,
                                         on_close=self.on_close)
        self.ws.on_open = self.on_open
        self.ws.run_forever()

    def on_message(self, ws, message):
        decoded_message = json.loads(message)

        # Extract bids
        bids = decoded_message.get("b", [])

        # Extract asks
        asks = decoded_message.get("a", [])
        
        last_five_bids = bids[:5]
        last_five_asks = asks[:5]
        
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        data=[{'ask':last_five_asks,'bids':last_five_bids ,'name':'binance','time':current_time,"pair":self.pair}]
        print(json.dumps(data, indent=4))

    def on_error(self, ws, error):
        print("Error:", error)

    def on_close(self, ws):
        print("Connection closed")

    def on_open(self, ws):
        print("Connection opened")
# Create an instance of the class
# ws = BinanceWebsocket()