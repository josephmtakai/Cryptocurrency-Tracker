# Cryptocurrency Tracker

This project is a simple cryptocurrency tracker that fetches real-time prices of selected cryptocurrencies using the CoinGecko API and visualizes the price trends over time using Plotly.

## Features

- Fetches real-time prices of cryptocurrencies (e.g., Bitcoin, Ethereum, Ripple)
- Collects data at regular intervals
- Visualizes the price trends with a line chart

## Prerequisites

- Python 3.x
- `requests` library
- `plotly` library

## Installation

1. Clone the repository to your local machine:

```bash
git clone https://github.com/yourusername/cryptocurrency-tracker.git
cd cryptocurrency-tracker

Create and activate a virtual environment:

On Windows:
Create and activate a virtual environment:
On Windows:
bash
Copy code
python -m venv .venv
.venv\Scripts\activate

On macOS/Linux:
bash
Copy code
python3 -m venv .venv
source .venv/bin/activate

Install the required packages:
bash
Copy code
pip install requests plotly
Usage
Ensure you are in the project directory and the virtual environment is activated.

Run the script:

bash
Copy code
python crypto_tracker.py
The script will fetch and display the current prices of the selected cryptocurrencies every minute, for a total of 10 minutes. After collecting the data, a Plotly graph will be displayed showing the price trends over time.
Example Output
The terminal will show the timestamps and prices for each cryptocurrency, and a Plotly graph will visualize the price trends.

SCREENSHOTS:
![TERMINAL](https://github.com/user-attachments/assets/8703c515-8e9f-466e-9214-0dd69e4b410d)
![REALTIME VISUALS](https://github.com/user-attachments/assets/a99bfd66-fc47-4212-83a8-0f04b0970a14)

2024-07-26 10:00:00 - bitcoin: $30000
2024-07-26 10:01:00 - ethereum: $2000
2024-07-26 10:02:00 - ripple: $0.5
...

Customization
Cryptocurrencies: You can change the cryptocurrencies being tracked by modifying the crypto_ids list in crypto_tracker.py.
Interval: Adjust the sleep time in the script to change the data collection interval.
Duration: Modify the loop range to collect data for a different number of iterations.
Contributing
Feel free to submit issues or pull requests if you have any improvements or suggestions.

License
This project is licensed under the MIT License - see the LICENSE file for details.

Acknowledgements
CoinGecko API for providing cryptocurrency data
Plotly for data visualization


Make sure to save this as `README.md` in the root of your project directory. You can customize the content to fit any additional features or modifications you add to your project.
