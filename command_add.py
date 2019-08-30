#!/usr/bin/env python3

from inventory import Inventory


def run(args):
    with Inventory(args.inventory) as inventory:
        inventory.add_item(args.item, args.count)
