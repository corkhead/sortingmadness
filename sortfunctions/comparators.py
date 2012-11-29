"""
Comparison functions

Arguments:
    a - first element to compare
    b - second element to compare
Returns:
    negative integer if the first precedes the second
    0 if both arguments have equal ordering
    positive integer if the first succeeds the second
"""

# Orders strings by their length.
def length(a, b):
    return len(a) - len(b)

# Orders strings alphabetically
def alpha(a, b):
    if (a < b):
        return -1
    elif (a == b):
        return 0
    else:
        return 1