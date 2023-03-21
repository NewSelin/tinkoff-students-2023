s = input().split()
stack = []
for l in s:
    if l in '+-*':
        y, x = stack.pop(), stack.pop()
    if l == '+':
        stack.append(x + y)
    elif l == '-':
        stack.append(x - y)
    elif l == "*":
        stack.append(x * y)
    else:
        stack.append(int(l))
print(stack.pop())