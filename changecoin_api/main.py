from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import requests

app = FastAPI()

# Add CORS middleware to allow requests from any origin
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins, adjust if needed
    allow_credentials=True,
    allow_methods=["*"],  # Allow all methods (GET, POST, etc.)
    allow_headers=["*"],  # Allow all headers
)


@app.get('/')
async def root():
    return {'message': 'Hello World'}


@app.get('/last_prices')
async def get_last_prices():
    url = 'https://api.coingecko.com/api/v3/simple/price?ids=bitcoin,ethereum,tether,binancecoin,solana,xrp,cardano,avalanche-2&vs_currencies=usd'
    res = requests.get(url)
    data = res.json()

    prices = {
        'Bitcoin': data['bitcoin']['usd'],
        'Ethereum': data['ethereum']['usd'],
        'Tether': data['tether']['usd'],
        'Binance Coin': data['binancecoin']['usd'],
        'Solana': data['solana']['usd'],
        'Cardano': data['cardano']['usd'],
        'Avalanche': data['avalanche-2']['usd'],
    }
    return prices


@app.get('/market_caps')
async def get_market_caps():
    url = 'https://api.coingecko.com/api/v3/simple/price?ids=bitcoin,ethereum,tether,binancecoin,solana,xrp,cardano,avalanche-2&vs_currencies=usd&include_market_cap=true'
    res = requests.get(url)
    data = res.json()

    prices = {
        'Bitcoin': data['bitcoin']['usd_market_cap'],
        'Ethereum': data['ethereum']['usd_market_cap'],
        'Tether': data['tether']['usd_market_cap'],
        'Binance Coin': data['binancecoin']['usd_market_cap'],
        'Solana': data['solana']['usd_market_cap'],
        'Cardano': data['cardano']['usd_market_cap'],
        'Avalanche': data['avalanche-2']['usd_market_cap'],
    }
    return prices
