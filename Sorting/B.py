n = int(input())
l = list(range(1, n+1))
for i in range(1, n):
    l[i//2], l[i] = l[i], l[i//2]
print(*l)