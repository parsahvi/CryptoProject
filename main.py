from binanceWebsocket import BinanceWebsocket
import btcturkWebsocket


import threading

def call_binance(pair):
    newPair = pair.lower()
    BinanceWebsocket(newPair)

def call_btcturk(pair):
    btcturkWebsocket.WebSocketManager(pair)
    
def process_broker(broker,pair):
    if broker == "binance":
        call_binance(pair)
    elif broker == "btcturk":
        call_btcturk(pair)


def main():
    avalable_pairs = ["BTCUSDT" , "ETHUSDT" , "LTCUSDT" , "ETHBTC" , "LTCBTC" , "ETHLTC"]
    avalable_brokers = ["binance", "btcturk"]

    print("Choose a pair from the following list -select number-: ")
    for i in range(len(avalable_pairs)):
        print(f"{i+1}. {avalable_pairs[i]}")
    pair = int(input())
    pair = avalable_pairs[pair-1]

    print("Choose one or more brokers from the following list -enter numbers separated by space-: ")
    for i in range(len(avalable_brokers)):
        print(f"{i+1}. {avalable_brokers[i]}")
    selected_brokers = input().split()
    selected_brokers = [avalable_brokers[int(broker)-1] for broker in selected_brokers]

    threads = []
    for broker in selected_brokers:
        thread = threading.Thread(target=process_broker, args=(broker,pair))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()
        
main()

