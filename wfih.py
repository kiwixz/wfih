#!/usr/bin/env python3

import argparse
import os

import command_add
import command_show
import command_update


def create_parser():
    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers(help="subcommands")

    parser.add_argument("-i", "--inventory", default="data/inventory.db", help="path to inventory database")
    parser.add_argument("-m", "--market", default="data/market.json", help="path to market database")

    parser_add = subparsers.add_parser("add", help="add an item to inventory")
    parser_add.set_defaults(command=command_add.run)
    parser_add.add_argument("item", nargs="?")
    parser_add.add_argument("count", nargs="?", default=1, type=int)

    parser_show = subparsers.add_parser("show", help="show full inventory")
    parser_show.set_defaults(command=command_show.run)
    parser_show.add_argument("-d", "--ducats", action="store_true", help="sort by ducats/price value")
    parser_show.add_argument("-p", "--plats", action="store_true", help="sort by price")

    parser_update = subparsers.add_parser("update")
    parser_update.set_defaults(command=command_update.run)

    return parser


if __name__ == "__main__":
    parser = create_parser()
    args = parser.parse_args()
    os.makedirs("data", exist_ok=True)
    if "command" in args:
        args.command(args)
    else:
        parser.print_help()
