from string import ascii_lowercase, ascii_uppercase

def parse_formula(s):
    def parse_digit():
        global ptr
        if len(s) > ptr and  s[ptr].isdigit():
            c = int(s[ptr])
            ptr += 1
            return c
        return None

    def parse_number():
        num = 0
        d = parse_digit()
        while d is not None:
            num = num * 10 + d
            d = parse_digit()
        return num

    def parse_him_element():
        global ptr
        if len(s) > ptr and  s[ptr] in ascii_uppercase:
            el = s[ptr]
            ptr += 1
            while len(s) > ptr and  s[ptr] in ascii_lowercase:
                el += s[ptr]
                ptr += 1
            return el
        else:
            return None

    def parse_element(num):
        global ptr
        if len(s) > ptr and s[ptr] == "(":
            ptr += 1
            dd = parse_sequence(num)
            if len(s) > ptr and s[ptr] == ")":
                ptr += 1
            return dd
        else:
            return parse_him_element()

    def add_to_dict(d, dd, num=1, num2=1):
        if isinstance(dd, str):
            if dd in d:
                d[dd] += (num * num2)
            else:
                d[dd] = (num * num2)
        else:
            for k in dd.keys():
                if k in d:
                    d[k] += dd[k]*num
                else:
                    d[k] = dd[k]*num

    def parse_sequence(num):
        global ptr
        dd = dict()
        el = parse_element(num)
        while el is not None:
            num2 = parse_number()
            if isinstance(el, dict):
                if num2 != 0:
                    add_to_dict(dd, el, num2)
                else:
                    add_to_dict(dd, el)
            else:
                if num2 != 0:
                    add_to_dict(dd, el, num, num2)
                else:
                    add_to_dict(dd, el, num)
            el = parse_element(num)
        return dd
    global ptr
    ptr = 0
    d = dict()
    while True:
        num = parse_number()
        if num == 0:
            num = 1
        dd = parse_sequence(num)
        add_to_dict(d, dd)
        if len(s) > ptr and s[ptr] == "+":
            ptr += 1
        else:
            break
    return d

s = input()
d = parse_formula(s)
for _ in range(int(input())):
    s1 = input()
    d1 = parse_formula(s1)
    if d == d1:
        print(f"{s}=={s1}")
    else:
        print(f"{s}!={s1}")