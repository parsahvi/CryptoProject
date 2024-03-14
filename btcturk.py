# import json
# import threading
# import time
# import websocket

# try:
#     import thread
# except ImportError:
#     import _thread as thread

# def on_message(ws, message):
#     decoded_message = json.loads(message)
#     asks = decoded_message[1]["AO"]
#     bids = decoded_message[1]["BO"]
    
#     last_five_bids = bids[:5]
#     last_five_asks = asks[:5]
    
#     print("Last five buy orders", last_five_bids)
#     print("Last five sell orders", last_five_asks)

# def on_error(ws, error):
#     print(error)

# def on_close(ws):
#     print("### closed ###")

# def on_open(ws):
#     def run(*args):
#         time.sleep(1)
#         message = [151,{"type":151,"channel":"orderbook","event":"BTCTRY","join":True}]
#         ws.send(json.dumps(message))
#     thread.start_new_thread(run, ())

# def reconnect_websocket_hourly():
#     # Define the function to reconnect the WebSocket
#     def reconnect():
#         print("Reconnecting WebSocket...")
#         ws.run_forever()

#     # Create a Timer object that runs the reconnect function every hour
#     timer = threading.Timer(3600, reconnect)
#     timer.start()

# if __name__ == "__main__":
#     # Create WebSocket connection
#     ws = websocket.WebSocketApp(
#         "wss://ws-feed-pro.btcturk.com/",
#         on_message=on_message,
#         on_error=on_error,
#         on_close=on_close)

#     # Set the on_open function
#     ws.on_open = on_open

#     # Start a new thread for reconnecting the WebSocket hourly
#     reconnect_websocket_hourly()

#     # Run WebSocket indefinitely
#     ws.run_forever()

import json
import threading
import time
import websocket

try:
    import thread
except ImportError:
    import _thread as thread

class WebSocketManager:
    def __init__(self, url):
        self.url = url
        self.ws = websocket.WebSocketApp(
            url,
            on_message=self.on_message,
            on_error=self.on_error,
            on_close=self.on_close)
        self.ws.on_open = self.on_open
        self.run_forever()
        self.reconnect_websocket_hourly()

    def on_message(self, ws, message):
        decoded_message = json.loads(message)
        asks = decoded_message[1]["AO"]
        bids = decoded_message[1]["BO"]
        
        last_five_bids = bids[:5]
        last_five_asks = asks[:5]
        
        print("Last five buy orders", last_five_bids)
        print("Last five sell orders", last_five_asks)

    def on_error(self, ws, error):
        print(error)

    def on_close(self, ws):
        print("### closed ###")

    def on_open(self, ws):
        def run(*args):
            time.sleep(1)
            message = [151,{"type":151,"channel":"orderbook","event":"BTCTRY","join":True}]
            ws.send(json.dumps(message))
        thread.start_new_thread(run, ())

    def run_forever(self):
        self.ws.run_forever()

    def reconnect_websocket_hourly(self):
        # Define the function to reconnect the WebSocket
        def reconnect():
            print("Reconnecting WebSocket...")
            self.ws.run_forever()

        # Create a Timer object that runs the reconnect function every hour
        timer = threading.Timer(3600, reconnect)
        timer.start()

if __name__ == "__main__":
    ws_manager = WebSocketManager("wss://ws-feed-pro.btcturk.com/")
