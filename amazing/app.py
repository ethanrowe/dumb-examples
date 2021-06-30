"""
This provides the entrypoint of an amazing application.
"""

import sys

from . import core

def express_amazement(degree):
    print("How amazing?")
    print(core.amaze(degree))
    print()

def main(args=None):
    if args is None:
        args = sys.argv[1:]
    if not(args):
        args = [core.MINIMAL_AMAZEMENT]
    for degree in args:
        express_amazement(int(degree))
    return 0

if __name__ == '__main__':
    sys.exit(main())

