EPSILON = 1e-8

def is_zero(x):
    return abs(x) < EPSILON

def equal(x, y):
    return abs(x - y) < EPSILON