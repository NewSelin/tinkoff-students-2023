n = int(input())
l = list(map(int, input().split()))


def count_inv(l, n):
    if n == 0:
        return [], 0
    if n == 1:
        return l, 0
    a1, a2 = count_inv(l[:n // 2], n // 2), count_inv(l[n // 2:], n - n // 2)
    return merge_inv(a1[0], a1[1], a2[0], a2[1])


def merge_inv(l1, inv1, l2, inv2):
    i1, i2 = 0, 0
    res = []
    inv = 0
    while i1 + i1 < len(l1) + len(l2):
        if l1[i1] <= l2[i2]:
            res.append(l1[i1])
            if i1 == len(l1) - 1:
                res.extend(l2[i2:])
                break
            i1 += 1
        else:
            res.append(l2[i2])
            inv += (len(l1) - i1)
            if i2 == len(l2) - 1:
                res.extend(l1[i1:])
                break
            i2 += 1
    return res, inv + inv1 + inv2


ans = count_inv(l, n)
print(ans[1])
print(*ans[0])
