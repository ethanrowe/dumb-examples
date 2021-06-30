"""
The core functionality of an application remarkable for its unremarkable nature.
"""

from importlib import resources
import json

MEDIOCRITY_DATABASE = json.load(
        resources.open_text(__package__, "mediocres.json"))

def mediocrity_selection(num, db=MEDIOCRITY_DATABASE):
    idx = num % len(db)
    return db[idx]

