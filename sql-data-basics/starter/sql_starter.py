"""Learner helper: run one SELECT at a time in local Python 3.

Keep schema.sql next to this file. Save your query in QUERY, then run:
python3 sql_starter.py
"""
import sqlite3
from pathlib import Path

QUERY = "SELECT id, title, capacity FROM workshops ORDER BY id"

with sqlite3.connect(":memory:") as connection:
    connection.execute("PRAGMA foreign_keys = ON")
    connection.executescript((Path(__file__).resolve().parent / "schema.sql").read_text())
    for row in connection.execute(QUERY):
        print(" | ".join(str(value) for value in row))
