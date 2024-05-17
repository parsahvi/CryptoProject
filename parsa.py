import threading 
import time

done = False

def process_text(input_text):
    count = 0
    while not done:
        time.sleep(1)
        count += 1
        # Removed debugging statement for better readability
        print(f"{input_text}:{count}")

threading.Thread(target=process_text, daemon=True, args=("fdsa",)).start()

input("Press enter to quit")
done = True 