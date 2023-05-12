import copy
n, m, k = map(int, input().split())
lst_ai = list(map(int, input().split()))

class Node:
    def __init__(self):
        self.next = {}
        self.count = 0
        self.terminal = False
        self.par = None
def add(root, s):
    node  = root
    for c in s:
        if c not in node.next:
            node.next[c] = Node()
        par_node = node
        node = node.next[c]
        node.par = par_node
        node.count += 1
    node.terminal = True

def dfs(node, sums, s, i):
    global ans, word
    if node.terminal:
        if sums < ans or ans == -1:
            ans = sums
            word = s
        return
    for c in [str(i) for i in range(k)]:
        if c not in node.next:
            s[i] = c
            if sums < ans or ans == -1:
                ans = sums
                word = s
                for j in range(i+1, m):
                    word[j] = "0"
            return
        else:
            node = node.next[c]
            s[i] = c
            if i == 0:
                sums += (node.count * lst_ai[i])
            else:
                sums += (node.count * (lst_ai[i] - lst_ai[i-1]))
            old_s = copy.copy(s)
            dfs(node, sums, s, i+1)
            s = copy.copy(old_s)
            if i == 0:
                sums -= (node.count * lst_ai[i])
            else:
                sums -= (node.count * (lst_ai[i] - lst_ai[i - 1]))
            node = node.par

root = Node()
for _ in range(n):
    st = input()
    add(root, st)
word = [''] * m
ans = -1
dfs(root, 0, [''] * m, 0)
s = ''
for c in word:
    s += c
print(s)
print(ans)
