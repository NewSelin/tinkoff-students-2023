s, t, p, m, pr, pows = input(), input(), 10**9 + 7, 179, [0], [1]
hash_t = 0
for c in t:
    hash_t = (hash_t*m + ord(c)) % p
for c in s:
    pr.append((pr[-1] * m + ord(c)) % p)
    pows.append(pows[-1]*m % p)
n = len(t)
for i in range(len(s)-n+1):
    if (pr[i+n] - pr[i] * pows[n]) % p == hash_t:
        print(i, end=" ")