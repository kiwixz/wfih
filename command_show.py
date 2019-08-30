#!/usr/bin/env python3

from inventory import Inventory


def run(args):
    with Inventory(args.inventory) as inventory:
        for item in inventory.get_items():
            print(f'{item["name"]}: {item["count"]}')
