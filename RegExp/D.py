import re
import sys
for line in sys.stdin:
    res = re.sub(r'\$v_{(.+)}\$', r'v[\1]',line)
    res = re.sub(r'\$v_(.)\$', r'v[\1]', res)
    print(res,end='')