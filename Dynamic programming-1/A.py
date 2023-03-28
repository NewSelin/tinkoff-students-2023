n = int(input())
lst = list(map(int, input().split()))
a, b = 0, lst[0]
for i in range(1, n):
    a, b = b, min(a + lst[i], b + lst[i])
print(b)