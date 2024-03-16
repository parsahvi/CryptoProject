import websocket
import json
class WebSocketManager:
    def __init__(self, url):
        self.url=url
        self.ws=websocket.WebSocketApp(url,
            on_message=self.on_message,
            on_error=self.on_error,
            on_close=self.on_close)
        self.ws.on_open = self.on_open
        self.run_forever()
    
    def on_message(self,ws,message):
        decoded_message = json.loads(message)

        # get buy data 
        bids = decoded_message.get("b", [])
        # get ask data 
        asks = decoded_message.get("a", [])
        # last five data
        last_five_bids = bids[:5]
        last_five_asks = asks[:5]
        print("Last five buy orders", last_five_bids)
        print("Last five sell orders", last_five_asks)
    
    
    def on_error(self, ws, error):
        print(error)

    def on_close(self, ws):
        print("### closed ###")
        # reconnect the connection
        self.ws.run_forever()
    
    def on_open(ws):
        print("Connection opened")

    def run_forever(self):
        self.ws.run_forever()
if __name__ == "__main__":
    ws_manager = WebSocketManager("wss://stream.binance.com:9443/ws/btcusdt@depth")