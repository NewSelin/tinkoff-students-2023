t, s, p, m, pr, pows, hash_t = input(), input(), 10**9 + 7, 179, [0], [1], [0]
for c in t:
    hash_t.append((hash_t[-1]*m + ord(c)) % p)
for c in s:
    pr.append((pr[-1] * m + ord(c)) % p)
    pows.append(pows[-1]*m % p)
n = len(t)
lst = []
def acc(i, j):
    ii = i
    while j - i > 1:
        m = (j+i) // 2
        if (pr[j] - pr[m] * pows[j-m]) % p == (hash_t[j-ii] - hash_t[m - ii] * pows[j - m]) % p:
            j = m
        elif (pr[m] - pr[i] * pows[m-i]) % p == (hash_t[m-ii] - hash_t[i - ii] * pows[m-i]) % p:
            i = m
        else:
            return False
    return True
for i in range(len(s)-n+1):
    if (pr[i+n] - pr[i] * pows[n]) % p == hash_t[-1] or acc(i, i+n):
        lst.append(i+1)
print(len(lst))
print(*lst)
