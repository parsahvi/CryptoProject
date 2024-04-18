import json
import threading
import time
import websocket
import Composition
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

    
    def on_message(self, ws, message):
        decoded_message = json.loads(message)

        # get ask data
        asks = decoded_message[1]["AO"]
        # get bay data
        bids = decoded_message[1]["BO"]
        
        # last five data 
        last_five_bids = bids[:5]
        last_five_asks = asks[:5]
        
        # print("Last five buy orders", last_five_bids)
        # print("Last five sell orders", last_five_asks)
        data=[{'ask':last_five_asks,'bids':last_five_bids ,'name':'btc'}]
        # print(data)
        Composition.test(data)
    def on_error(self, ws, error):
        print(error)

    def on_close(self, ws):
        print("### closed ###")
        # if serve close the connection
        self.reconnect_websocket_hourly()

    def on_open(self, ws):
        def run(*args):
            time.sleep(1)
            message = [151,{"type":151,"channel":"orderbook","event":"BTCTRY","join":True}]
            ws.send(json.dumps(message))
        thread.start_new_thread(run, ())

    def run_forever(self):
        self.ws.run_forever()

    def reconnect_websocket_hourly(self):
        def reconnect():
            print("Reconnecting WebSocket...")
            self.ws.run_forever()

        timer = threading.Timer(3600, reconnect)
        timer.start()

if __name__ == "__main__":
    ws_manager = WebSocketManager("wss://ws-feed-pro.btcturk.com/")
