import json
import pprint
import time
import websocket

try:
    import thread
except ImportError:
    import _thread as thread

def on_message(ws, message):


    decoded_message = json.loads(message)
    # pprint.pprint(decoded_message[1]["AO"])
    # pprint.pprint(decoded_message)
    # asks = decoded_message.get(decoded_message[1]["AO"])
    # bids = decoded_message.get("BO", [])
    # last_five_bids = bids[:5]
    # last_five_asks = asks[:5]
    # print("Last five buy orders", last_five_bids)
    # print("Last five sell orders", last_five_asks)
    # pprint.pprint(decoded_message[1]["AO"])
    asks = decoded_message[1]["AO"]
    bids = decoded_message[1]["BO"]
    
    last_five_bids = bids[:5]
    last_five_asks = asks[:5]
    
    print("Last five buy orders", last_five_bids)
    print("Last five sell orders", last_five_asks)

def on_error(ws, error):
    print(error)

def on_close(ws):
    print("### closed ###")

    
def on_open(ws):
    def run(*args):
        time.sleep(1)
        message = [151,{"type":151,"channel":"orderbook","event":"BTCTRY","join":True}]
        ws.send(json.dumps(message))
    thread.start_new_thread(run, ())


if __name__ == "__main__":
    # websocket.enableTrace(True)
    ws = websocket.WebSocketApp(
        "wss://ws-feed-pro.btcturk.com/",
        on_message=on_message,
        on_error=on_error,
        on_close=on_close)
    ws.on_open = on_open
    ws.run_forever()
    
    
#export :    
# Last five sell orders [
#     {'A': '0.003584755872', 'P': '2365749'}
#     , {'A': '0.00038912', 'P': '2365940'}
#     , {'A': '0.02057192', 'P': '2366940'}
#     , {'A': '0.01', 'P': '2366948'}
#     , {'A': '0.01241117', 'P': '2366958'}]