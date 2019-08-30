#!/usr/bin/env python3

from inventory import Inventory
from market import Market


def run(args):
    with Inventory(args.inventory) as inventory:
        item = Market(args.market).guess_name(args.item)
        inventory.add_item(item, args.count)
        if args.count < 0:
            print(f'removed {-args.count}x {item} from inventory')
        else:
            print(f'added {args.count}x {item} to inventory')
