from random import random


class Node:
    def __init__(self, x):
        self.x = x
        self.y = random()
        self.l = None
        self.r = None
def split(S, x):
    if S is None:
        return None, None
    if S.x < x:
        S.r, r = split(S.r, x)
        return S, r
    else:
        l, S.l = split(S.l, x)
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
        l.r = merge(l.r, r)
        return l
    else:
        r.l = merge(l, r.l)
        return r
def next(S, i):
    l, r = split(S, i)
    m = min_treap(r)
    S = merge(l, r)
    return m
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
for _ in range(n):
    cmd, val = input().split()
    if cmd == "+":
        val = (int(val) + last_get) % (10**9)
        last_get = 0
        if S is None:
            S = Node(int(val))
        else:
            S = add(S, int(val))
    else:
        last_get = next(S, int(val))
        print(last_get)