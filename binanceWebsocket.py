# import threading
# import websocket
# import json
# import time

# class BinanceWebsocket:
#     def on_message(self, ws, message):
#         decoded_message = json.loads(message)

#         # Extract bids
#         bids = decoded_message.get("b", [])

#         # Print A (price) and B (quantity) for each bid entry
#         # for bid_entry in bids:
#         #     price, quantity = bid_entry
#         #     print("Buy Order Price", price,"\n", "Buy order Quantity", quantity)
            
#         # # Extract asks
#         asks = decoded_message.get("a", [])
        
#         # # Print A (price) and B (quantity) for each ask entry
#         # for ask_entry in asks:
#         #     price, quantity = ask_entry
#         #     print("Sell Order Price", price,"\n", "Sell order Quantity", quantity)
            
#         last_five_bids = bids[:5]
#         last_five_asks = asks[:5]
        
#         print("Last five buy orders", last_five_bids)
#         print("Last five sell orders", last_five_asks)

        
#     def on_error(self, ws, error):
#         print("Error:", error)

#     def on_close(self, ws):
#         print("Connection closed")
#         get_data_with_websocket()

#     def on_open(self, ws):
#         print("Connection opened")

#     def get_data_with_websocket(self):
#         # websocket.enableTrace(True)
#         ws = websocket.WebSocketApp("wss://stream.binance.com:9443/ws/btcusdt@depth",  
#                                     on_message=on_message,
#                                     on_error=on_error,
#                                     on_close=on_close)
#         ws.on_open = on_open
#         ws.run_forever()

#     get_data_with_websocket()
import websocket
import json
import time
import Composition
from datetime import datetime
class BinanceWebsocket:
    def __init__(self):
        self.ws = websocket.WebSocketApp("wss://stream.binance.com:9443/ws/btcusdt@depth",  
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
        data=[{'ask':last_five_asks,'bids':last_five_bids ,'name':'binance','time':current_time}]
        Composition.dataGetter(data)
        
        # print("Last five buy orders", last_five_bids)
        # print("Last five sell orders", last_five_asks)

    def on_error(self, ws, error):
        print("Error:", error)

    def on_close(self, ws):
        print("Connection closed")

    def on_open(self, ws):
        print("Connection opened")

# Create an instance of the class
# ws = BinanceWebsocket()