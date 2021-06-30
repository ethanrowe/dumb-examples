"""
This is the core functionality of an amazing application.
"""

MINIMAL_AMAZEMENT = 2

def amaze(degree):
    assert degree >= MINIMAL_AMAZEMENT, "Only true amazement is acceptable."
    amazement = "o" * degree
    return f"S{amazement} amazing."

