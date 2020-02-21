#!/usr/bin/env python3

import urllib.request


def run(args):
    urllib.request.urlretrieve("https://wf.kwx.gg/market_prices.json", args.market)
    print("updated market prices")
