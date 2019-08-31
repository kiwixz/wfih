#!/usr/bin/env python3

from inventory import Inventory
from market import Market


def run(args):
    market = Market(args.market)
    with Inventory(args.inventory) as inventory:
        items = ({'name': item['name'],
                  'count': item['count'],
                  'market': market.item(item['name'])}
                 for item in inventory.get_items())

        if args.ducats:
            items = sorted(items, key=lambda a: -a["market"]["ducats"] / a['market']['stats'][-1]['median'])
        else:
            items = sorted(items, key=lambda a: -a['market']['stats'][-1]['median'])

        print(f'{"Ducats/Price":>60} {"Volume":>9} {"Price":>9}')
        for item in items:
            label = f'{item["count"]}x {item["name"].replace("_", " ").title()}'
            market_stats = item['market']['stats'][-1]
            ducats = item["market"]["ducats"] / market_stats["median"]
            print(f'{label:50} {ducats:9.2f} {market_stats["volume"]:9} {market_stats["median"]:9.2f}')
