"""Frequencies function."""
"""ENTER YOUR SOLUTION HERE!"""

def frequencies(items):
    frequencies = {}
    # Your code goes here
    for item in items:
        if not isinstance(item, str):
            item = str(item)
        keys = frequencies.keys()

        if item not in keys:
            frequencies[item] = 1
        else:
            frequencies[item] = frequencies.get(item) + 1
    return frequencies
