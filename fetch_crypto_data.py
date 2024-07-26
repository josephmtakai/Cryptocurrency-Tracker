import requests
import time

def fetch_crypto_data(crypto_id):
    url = f'https://api.coingecko.com/api/v3/simple/price?ids={crypto_id}&vs_currencies=usd'
    response = requests.get(url)
    data = response.json()
    return data[crypto_id]['usd']

if __name__ == "__main__":
    crypto_id = 'bitcoin'  # You can change this to any other cryptocurrency ID
    price = fetch_crypto_data(crypto_id)
    print(f"The current price of {crypto_id} is ${price}")
