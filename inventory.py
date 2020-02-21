#!/usr/bin/env python3

import sqlite3


class Inventory:
    def __init__(self, file):
        self.db = sqlite3.connect(file)
        self.db.row_factory = sqlite3.Row
        self.db.execute(
            """CREATE TABLE IF NOT EXISTS items_v1 (
                   name TEXT NOT NULL UNIQUE
                 , count INTEGER NOT NULL CHECK(count >= 0)
               );"""
        )

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        if exc_type is None:
            self.db.commit()
        else:
            self.db.rollback()
        self.db.close()
        return False

    def get_items(self):
        return self.db.execute("SELECT * FROM items_v1 WHERE count > 0").__iter__()

    def add_item(self, item, count):
        self.db.execute(
            """INSERT OR REPLACE INTO items_v1 (name, count)
                   VALUES (?, COALESCE((SELECT count FROM items_v1 WHERE name LIKE ?), 0) + ?)""",
            (item, item, count),
        )
