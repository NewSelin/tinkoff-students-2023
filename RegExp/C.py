import re
import sys
for line in sys.stdin:
    line = line.replace("\\", "\\\\")
    res = re.sub('\\\\circle{\((\d+),(\d+)\)', '\\\\circle{(\\2,\\1)', line)
    print(res.replace("\\\\", "\\"), end='')