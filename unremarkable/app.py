"""
The entrypoint for an unremarkable application about unremarkable people.
"""

import json
import sys
from . import core

def report(selection):
    out = {"unremarkable_person": selection}
    print(json.dumps(selection, sort_keys=True))

def get_input_stream():
    for item in sys.stdin:
        yield item.strip()

def main(args=None):
    items = args
    if not items:
        items = get_input_stream()
    for item in items:
        selection = core.mediocrity_selection(int(item))
        report(selection)
    return 0

if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))

