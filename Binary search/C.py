import sys

r = int(input())


def query(x):
    print(x)
    sys.stdout.flush()
    return input()


l = 1
while True:
    if l + 1 == r or r == 1:
        if query(r) == ">=":
            print("! " + str(r))
        else:
            print("! " + str(l))
        break
    if query((l + r) // 2) == "<":
        r = (l + r) // 2
    else:
        l = (l + r) // 2
