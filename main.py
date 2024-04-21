from binanceWebsocket import BinanceWebsocket
from btcturkWebsocket import WebSocketManager

avalable_pairs = ["btcusdt"]

avalable_brokers = ["binance" ,"btcturk"]
# Ask for user input for the pair and broker
# List of all the available pairs
# List of all the avalable brokers
print("Choose a pair from the following list -select number-: ")
for i in range(len(avalable_pairs)):
    print(f"{i+1}. {avalable_pairs[i]}")
pair = int(input())
pair = avalable_pairs[pair-1]

print("Choose a broker from the following list -select number-: ")
for i in range(len(avalable_brokers)):
    print(f"{i+1}. {avalable_brokers[i]}")
broker = int(input())
broker = avalable_brokers[broker-1]

switcher = {
    "binance": BinanceWebsocket,
    "btcturk": WebSocketManager
}

# Get the class from the switcher dictionary
BrokerClass = switcher.get(broker)

# Create an instance of the class
ws = BrokerClass()