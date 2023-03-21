s, m, p, t, pr, pows = input(), int(input()), 10**9 + 7, 179, [0], [1]
for c in s:
    pr.append((pr[-1] * t + ord(c)) % p)
    pows.append(pows[-1]*t % p)
def hash(a, b):
    return (pr[b] - pr[a-1] * pows[b-a+1]) % p
for _ in range(m):
    a, b, c, d = map(int, input().split())
    if hash(a, b) == hash(c, d):
        print("Yes")
    else:
        print("No")