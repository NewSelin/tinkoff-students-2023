from random import randint
from collections import Counter
n = int(input())
a = input().split()
m = int(input())
b = input().split()
c = 10**9 + 7
pr1 = [0]
pr2 = [0]
hash_t = dict()
for i in range(n):
    if a[i] not in hash_t:
        hash_t[a[i]] = randint(1, 100000)
    pr1.append((pr1[-1] + hash_t[a[i]]) % c)
for i in range(m):
    if b[i] not in hash_t:
        hash_t[b[i]] = randint(1, 100000)
    pr2.append((pr2[-1] + hash_t[b[i]]) % c)
def f(pr1, pr2, n, m, aa, bb):
    mm = n
    y = False
    while mm != 0:
        hash_pr_1 = set()
        for i in range(n-mm+1):
            hash_pr_1.add(pr1[i+mm] - pr1[i])
        for j in range(m-mm+1):
            if pr2[j+mm] - pr2[j] in hash_pr_1:
                for i in range(n - mm + 1):
                    if pr1[i + mm] - pr1[i] == pr2[j + mm] - pr2[j]:
                        if Counter(aa[i: i + mm]) == Counter(bb[j: j + mm]):
                            y = True
                            break
                if y:
                    break
        if y:
            break
        mm -= 1
    return mm
if n > m:
    print(f(pr2, pr1, m, n, b, a))
else:
    print(f(pr1, pr2, n, m, a, b))