#!/usr/bin/env python3

from inventory import Inventory
from market import Market


def run(args):
    market = Market(args.market)
    with Inventory(args.inventory) as inventory:
        items = ({'name': item['name'],
                  'count': item['count'],
                  'stats': market.stats(item['name'])}
                 for item in inventory.get_items())
        items = sorted(items, key=lambda a: -a["stats"]["median"])

        print(f'{"":60} {"Volume":>9} {"Price":>9}')
        for item in items:
            label = f'{item["count"]}x {item["name"].replace("_", " ").title()}'
            volume = item["stats"]["volume"]
            price = item["stats"]["median"]
            print(f'{label:60} {volume:9} {price:9}')
