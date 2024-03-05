import threading
import websocket
import json
import time

def on_message(ws, message):
    print("Received message:", message)
    
def on_error(ws, error):
    print("Error:", error)

def on_close(ws):
    print("Connection closed")
    get_data_with_websocket()

def on_open(ws):
    print("Connection opened")

def get_data_with_websocket():
    websocket.enableTrace(True)
    ws = websocket.WebSocketApp("wss://stream.binance.com:9443/ws/btcusdt@depth",  
                                on_message=on_message,
                                on_error=on_error,
                                on_close=on_close)
    ws.on_open = on_open
    ws.run_forever()

get_data_with_websocket()