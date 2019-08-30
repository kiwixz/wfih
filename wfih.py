#!/usr/bin/env python3

import argparse

import command_add
import command_show
import command_top


def parse_args():
    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers(help="subcommands")

    parser.add_argument('-i', '--inventory', default='data/inventory.db', help='path to inventory database')

    parser_add = subparsers.add_parser('add', help='add an item to inventory')
    parser_add.set_defaults(command=command_add.run)
    parser_add.add_argument('item')
    parser_add.add_argument('count', nargs='?', default=1, type=int)

    parser_top = subparsers.add_parser('show', help='show full inventory')
    parser_top.set_defaults(command=command_show.run)

    parser_top = subparsers.add_parser('top', help='sort inventory by value')
    parser_top.set_defaults(command=command_top.run)

    return parser.parse_args()


if __name__ == '__main__':
    args = parse_args()
    args.command(args)
