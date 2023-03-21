from collections import deque
n = int(input())
q_l, q_r = deque(), deque()
for _ in range(n):
    s = input().split()
    if s[0] == '+':
        q_r.append(s[1])
    if s[0] == '*':
        while len(q_r) > len(q_l):
            a = q_r.popleft()
            q_l.append(a)
        q_r.appendleft(s[1])
    if s[0] == '-':
        while len(q_r) > len(q_l):
            a = q_r.popleft()
            q_l.append(a)
        print(q_l.popleft())

