import requests
import time
import datetime
import plotly.graph_objects as go

def fetch_crypto_data(crypto_id):
    url = f'https://api.coingecko.com/api/v3/simple/price?ids={crypto_id}&vs_currencies=usd'
    response = requests.get(url)
    data = response.json()
    return data[crypto_id]['usd']

if __name__ == "__main__":
    crypto_ids = ['bitcoin', 'ethereum', 'ripple']
    prices = {crypto_id: [] for crypto_id in crypto_ids}
    timestamps = []
    
    for _ in range(10):  # Collect data 10 times
        timestamp = datetime.datetime.now()
        timestamps.append(timestamp)
        
        for crypto_id in crypto_ids:
            price = fetch_crypto_data(crypto_id)
            prices[crypto_id].append(price)
            print(f"{timestamp} - {crypto_id}: ${price}")
        
        time.sleep(60)  # Wait for 1 minute before fetching data again

    # Create a line chart for each cryptocurrency
    fig = go.Figure()
    for crypto_id in crypto_ids:
        fig.add_trace(go.Scatter(x=timestamps, y=prices[crypto_id], mode='lines', name=f'{crypto_id.capitalize()} Price'))
    
    fig.update_layout(title='Cryptocurrency Prices Over Time', xaxis_title='Time', yaxis_title='Price (USD)')
    fig.show()
