import requests
import time
import datetime

def fetch_crypto_data(crypto_id):
    url = f'https://api.coingecko.com/api/v3/simple/price?ids={crypto_id}&vs_currencies=usd'
    response = requests.get(url)
    data = response.json()
    return data[crypto_id]['usd']

if __name__ == "__main__":
    crypto_id = 'bitcoin'
    prices = []
    timestamps = []
    
    for _ in range(10):  # Collect data 10 times
        price = fetch_crypto_data(crypto_id)
        timestamp = datetime.datetime.now()
        prices.append(price)
        timestamps.append(timestamp)
        print(f"{timestamp}: ${price}")
        time.sleep(60)  # Wait for 1 minute before fetching data again
