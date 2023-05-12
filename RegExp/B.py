import re
s = input()
t = ""
while t != s:
    t = s
    s = re.sub(r'(\W)the(\W)', r'\1\2', s, flags=re.I)
    s = re.sub(r'(\W)a(\W)', r'\1\2', s, flags=re.I)
    s = re.sub(r'(\W)an(\W)', r'\1\2', s, flags=re.I)
    s = re.sub(r'^the(\W)', r'\1', s, flags=re.I)
    s = re.sub(r'^a(\W)', r'\1', s, flags=re.I)
    s = re.sub(r'^an(\W)', r'\1', s, flags=re.I)
    s = re.sub(r'(\W)the$', r'\1', s, flags=re.I)
    s = re.sub(r'(\W)a$', r'\1', s, flags=re.I)
    s = re.sub(r'(\W)an$', r'\1', s, flags=re.I)
t = ""
while t != s:
    t = s
    s = re.sub(r'Ci', r'Si', s)
    s = re.sub(r'ci', r'si', s)
    s = re.sub(r'Ce', r'Se', s)
    s = re.sub(r'ce', r'se', s)
    s = re.sub(r'Ck|C', r'K', s)
    s = re.sub(r'ck|c', r'k', s)
t = ""
while t != s:
    t = s
    s = re.sub(r'Ee', r'I', s)
    s = re.sub(r'ee', r'i', s)
    s = re.sub(r'Oo', r'U', s)
    s = re.sub(r'oo', r'u', s)
    s = re.sub(r'([a-zA-Z])\1', r'\1', s, flags=re.I)
t = ""
while t != s:
    t = s
    s = re.sub(r'([a-zA-Z])e ', r'\1 ', s)
s = re.sub(r'\s+', r' ', s)
s = re.sub(r'^\s', r'', s)
s = re.sub(r'\s$', r'', s)
print(s)
