s, p, t = input(), 10**9 + 7, 179
n = len(s)
pr, pows, suff =  [0] * (n+1), [1] * (n+1), [0] * (n+1)
for i in range(n):
    pr[i+1] = (pr[i] * t + ord(s[i]))%p
    pows[i+1] = pows[i]*t % p
    suff[n-i-1] = (suff[n-i]*t + ord(s[n-i-1]))%p
def get_hash(a, b):
    return (pr[b] - pr[a-1] * pows[b-a+1]) % p
def get_rev_hash(a, b):
    return (suff[a-1] - suff[b] * pows[b-a+1]) % p
ans = 0
for i in range(n):
    l1 = l2 = 1
    r1 = min(i+1, n-i)
    r2 = min(i, n-i)
    v1 = v2 = 0
    while l1 <= r1:
        m = (l1 + r1) // 2
        if get_hash(i-m+2, i+m) == get_rev_hash(i-m+2, i+m):
            v1 = m
            l1 = m+1
        else:
            r1 = m-1
    ans += v1
    while l2 <= r2:
        m = (l2 + r2) // 2
        if get_hash(i-m+1, i+m) == get_rev_hash(i-m+1, i+m):
            v2 = m
            l2 = m+1
        else:
            r2 = m-1
    ans += v2
print(ans)