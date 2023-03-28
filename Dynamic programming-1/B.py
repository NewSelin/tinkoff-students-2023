n = int(input())
prev_not_A, prev_A = 2, 1
for i in range(1, n):
    prev_not_A, prev_A = (prev_not_A + prev_A) * 2, prev_not_A
print(prev_not_A + prev_A)