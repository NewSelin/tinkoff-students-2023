from string import ascii_uppercase
n = int(input())
s = input()
ascii_dict = dict()
for l in ascii_uppercase:
        ascii_dict[l] = 0
for l in s:
    ascii_dict[l] += 1
pal = ''
m = ''
b = True
for l, i in ascii_dict.items():
    if i % 2 == 1 and b:
        m = l
        b = False
    pal += l*(i//2)
print(pal + m + pal[::-1])