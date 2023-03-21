import sys
from functools import cmp_to_key
l = [l.strip() for l in sys.stdin]
def compare(x, y):
    if x + y > y + x:
        return -1
    elif x == y:
        return 0
    else:
        return 1
print(''.join(sorted(l, key=cmp_to_key(compare))))