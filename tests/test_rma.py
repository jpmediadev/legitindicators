import requests
from src.rma import rma

BINANCE_URL = "https://api.binance.com/api/v3/klines"
SYMBOL = "BTCUSDT"
INTERVAL = "1h"
PARAMS = {"symbol":SYMBOL, "interval":INTERVAL}

def test_rma():
    response = requests.get(url = BINANCE_URL, params = PARAMS)
    data = response.json()
    close = [float(d[4]) for d in data]
    r = rma(close,10)
    print(r)
    assert len(r) == len(close)
