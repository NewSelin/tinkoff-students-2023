n = int(input())
l = [-1] + list(map(int, input().split())) + [-1]
stack = [0]
help_l = []
for i in range(1, n+1):
    while l[stack[-1]] >= l[i]:
        stack.pop()
    help_l.append(stack[-1])
    stack.append(i)
help_r = []
stack = [n+1]
for i in range(n, 0, -1):
    while l[stack[-1]] >= l[i]:
        stack.pop()
    help_r.append(stack[-1])
    stack.append(i)
prefix_sum = [0]
for i in l[1: n+1]:
    prefix_sum.append(prefix_sum[-1] + i)
m = 0
for i in range(n):
    new_m = (prefix_sum[help_r[n-i-1]-1] - prefix_sum[help_l[i]]) * l[i+1]
    if new_m > m:
        m = new_m
print(m)