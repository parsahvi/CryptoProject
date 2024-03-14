# import websockets
# import json

# def on_message(ws, message):
#     print("Received message:", message)

# def on_error(ws, error):
#     print("Error:", error)

# def on_close(ws):
#     print("Connection closed")

# def on_open(ws):
#     print("Connection opened")
#     request_data = {"action": "get_data"}  
#     ws.send(json.dumps(request_data))

# def get_data_with_websocket():
#     websockets.enableTrace(True)
#     ws = websockets.WebSocketApp("wss://example.com/socket",  
#     on_message=on_message,
#     on_error=on_error,
#     on_close=on_close)
#     ws.on_open = on_open
#     ws.run_forever()

# get_data_with_websocket()


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
    request_data = {"action": "get_data"}  
    ws.send(json.dumps(request_data))

def get_data_with_websocket():
    websocket.enableTrace(True)
    ws = websocket.WebSocketApp("wss://example.com/socket",  
                                on_message=on_message,
                                on_error=on_error,
                                on_close=on_close)
    ws.on_open = on_open
    ws.run_forever()

def check_and_reconnect():
    while True:
        time.sleep(3600)  
        if not ws.connected:
            print("Connection lost, reconnecting...")
            get_data_with_websocket()

thread = threading.Thread(target=check_and_reconnect)
thread.start()

get_data_with_websocket()