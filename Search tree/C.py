from random import random


class Node:
    def __init__(self, x):
        self.x = x
        self.y = random()
        self.l = None
        self.r = None
        self.k = 1
def split(S, x):
    if S is None:
        return None, None
    if S.x <= x:
        S.r, r = split(S.r, x)
        if r:
            S.k -= r.k
        return S, r
    else:
        l, S.l = split(S.l, x)
        if l:
            S.k -= l.k
        return l, S
def merge(l, r):
    if l is None:
        return r
    if r is None:
        return l
    if l.y > r.y:
        l.k += r.k
        l.r = merge(l.r, r)
        return l
    else:
        r.k += l.k
        r.l = merge(l, r.l)
        return r
def add(S, i):
    l, r = split(S, i)
    l = merge(l, Node(i))
    S = merge(l, r)
    return S
def remove(S, i):
    l, r = split(S, i - 1)
    _, r = split(r, i)
    S = merge(l, r)
    return S
def find_k(S, i):
    if S.r is None:
        if i == 1:
            return S.x
        else:
            return find_k(S.l, i-1)
    if S.r.k + 1 == i:
        return S.x
    elif S.r.k + 1 > i:
        return find_k(S.r, i)
    else:
        return find_k(S.l, i - S.r.k - 1)
n = int(input())
S = None
for q in [input().split() for _ in range(n)]:
    if q[0] == "+1" or q[0] == "1":
        if S is None:
            S = Node(int(q[1]))
        else:
            S = add(S, int(q[1]))
    elif q[0] == "-1":
        S = remove(S, int(q[1]))
    else:
        print(find_k(S, int(q[1])))