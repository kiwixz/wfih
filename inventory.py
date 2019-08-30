#!/usr/bin/env python3

import sqlite3


class Inventory:
    def __init__(self, file):
        self.db = sqlite3.connect(file)

    def __enter__(self):
        pass

    def __exit__(self, exc_type, exc_value, traceback):
        self.db.commit()
        self.db.close()
        return False
