#!/usr/bin/env python3

from inventory import Inventory
from market import Market


def run(args):
    market = Market(args.market)
    with Inventory(args.inventory) as inventory:
        def add(item):
            item = market.guess_name(item)
            inventory.add_item(item, args.count)
            if args.count < 0:
                print(f'removed {-args.count}x {item} from inventory')
            else:
                print(f'added {args.count}x {item} to inventory')

        if args.item is None:
            while True:
                item = input('> ')
                if not item:
                    break
                add(item)
        else:
            add(args.item)
