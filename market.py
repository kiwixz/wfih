#!/usr/bin/env python3

import json


class Market:
    def __init__(self, file):
        with open(file, 'r') as f:
            self.db = json.load(f)['items']

    def find_item(self, item):
        if item in self.db:
            return item
        raise Exception('could not find item')
