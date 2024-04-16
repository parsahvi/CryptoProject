import threading
import websocket
import json
import time

def on_message(ws, message):
    decoded_message = json.loads(message)
    print(message)

    # Extract bids
    # bids = decoded_message.get("b", [])

    # Print A (price) and B (quantity) for each bid entry
    # for bid_entry in bids:
    #     price, quantity = bid_entry
    #     print("Buy Order Price", price,"\n", "Buy order Quantity", quantity)
        
    # # Extract asks
    # asks = decoded_message.get("a", [])
    
    # # Print A (price) and B (quantity) for each ask entry
    # for ask_entry in asks:
    #     price, quantity = ask_entry
    #     print("Sell Order Price", price,"\n", "Sell order Quantity", quantity)
        
    # last_five_bids = bids[:5]
    # last_five_asks = asks[:5]
    
    # print("Last five buy orders", last_five_bids)
    # print("Last five sell orders", last_five_asks)

        
def on_error(ws, error):
    print("Error:", error)

def on_close(ws):
    print("Connection closed")
    get_data_with_websocket()

def on_open(ws):
    print("Connection opened")

def get_data_with_websocket():
    # websocket.enableTrace(True)
    ws = websocket.WebSocketApp("wss://wsapi.nobitex.ir/socket.io/?EIO=3&transport=websocket",  
                                on_message=on_message,
                                on_error=on_error,
                                on_close=on_close)
    ws.on_open = on_open
    ws.run_forever()

get_data_with_websocket()