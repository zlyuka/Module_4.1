from math import inf

def divide(first, second):
    if second == 0:
        return inf
    else:
        a = first / second
        return int(a)

