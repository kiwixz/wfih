#!/usr/bin/env python3

import difflib
import json


class Market:
    def __init__(self, file):
        with open(file, 'r') as f:
            self.db = json.load(f)['items']

    def guess_name(self, item):
        matches = difflib.get_close_matches(item, self.db.keys(), 1, 0.1)
        if not matches:
            raise Exception('could not find item')
        return matches[0]

    def stats(self, item):
        return self.db[item]['stats'][-1]
