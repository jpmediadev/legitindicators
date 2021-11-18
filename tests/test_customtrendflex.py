import requests
from legitindicators import custom_trendflex

BINANCE_URL = "https://api.binance.com/api/v3/klines"
SYMBOL = "BTCUSDT"
INTERVAL = "1h"
PARAMS = {"symbol": SYMBOL, "interval": INTERVAL}


def test_custom_trendflex():
    response = requests.get(url=BINANCE_URL, params=PARAMS)
    data = response.json()
    close = [float(d[4]) for d in data]
    tf = custom_trendflex(close, 40, 10)
    print(tf)
    assert len(tf) == len(close)
