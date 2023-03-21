from random import random


class Node:
    def __init__(self, x):
        self.x = x
        self.y = random()
        self.l = None
        self.r = None
        self.s = x
def split(S, x):
    if S is None:
        return None, None
    if S.x < x:
        S.r, r = split(S.r, x)
        if r:
            S.s -= r.s
        return S, r
    else:
        l, S.l = split(S.l, x)
        if l:
            S.s -= l.s
        return l, S
def min_treap(S):
    if S is None:
        return -1
    if S.l is None:
        return S.x
    else:
        return min_treap(S.l)

def merge(l, r):
    if l is None:
        return r
    if r is None:
        return l
    if l.y > r.y:
        l.s += r.s
        l.r = merge(l.r, r)
        return l
    else:
        r.s += l.s
        r.l = merge(l, r.l)
        return r
def summ(S, i1, i2):
    l, r = split(S, i1)
    lr, rr = split(r, i2 + 1)
    if lr is None:
        s = 0
    else:
        s = lr.s
    S = merge(l, merge(lr, rr))
    return s
def add(S, i):
    l, r = split(S, i)
    if min_treap(r) != i:
        S = merge(merge(l, Node(i)), r)
    else:
        S = merge(l, r)
    return S
n = int(input())
S = None
last_get = 0
for q in [input().split() for _ in range(n)]:
    if q[0] == "+":
        val = (int(q[1]) + last_get) % (10**9)
        last_get = 0
        if S is None:
            S = Node(val)
        else:
            S = add(S, val)
    else:
        last_get = summ(S, int(q[1]), int(q[2]))
        print(last_get)