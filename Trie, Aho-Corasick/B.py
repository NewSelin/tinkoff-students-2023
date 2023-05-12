from sys import setrecursionlimit
setrecursionlimit(100000)
def num(c):
    return ord(c) - ord("a")
class Node:
    def __init__(self, alpha, parent, pchar, l):
        self.go = [None] * alpha
        self.terminal = False
        self.parent = parent
        self.pchar = pchar
        self.sufflink = None
        self.l = l

def add(root, s, j):
    node, l = root, 0
    for c in s:
        l += 1
        if node.go[num(c)] is None:
            node.go[num(c)] = Node(26, node, c, l)
        node = node.go[num(c)]
    node.terminal = True
    if node in ans:
        ans[node][0].append(j)
    else:
        ans[node] = ([j], [])

def get_sufflink(node, root):
    if node.sufflink is not None:
        return node.sufflink
    if node == root or node.parent == root:
        node.sufflink = root
    else:
        node.sufflink = get_go(get_sufflink(node.parent, root), node.pchar, root)
    return node.sufflink

def get_go(node, c, root):
    if node.go[num(c)] is not None:
        return node.go[num(c)]
    elif node == root:
        node.go[num(c)] = root
    else:
        node.go[num(c)] = get_go(get_sufflink(node, root), c, root)
    return node.go[num(c)]

ans = dict()
s = input().strip()
n = int(input())
root = Node(26, None, None, 0)
j = 0
for _ in range(n):
    add(root, input().strip(), j)
    j += 1

node = root
for i in range(len(s)):
    node = get_go(node, s[i], root)
    v = node
    while v != root:
        if v.terminal:
            ans[v][1].append(i - v.l + 2)
        v = get_sufflink(v, root)

new_ans = []
for t in ans.values():
    for i in t[0]:
        new_ans.append((i, t[1]))
ans = sorted(new_ans, key=lambda x: x[0])
ans = list(map(lambda x: [len(x[1])] + x[1], ans))
for lst in ans:
   print(*lst)