import sys

strn = []
for s in sys.stdin:
    strn.append(s)

strng = ''.join(strn).lower()

a = 'abcdefghijklmnopqrstuvwxyz'

strng_lower = strng.lower()

for i in range(26):
    print("{} : {}".format(a[i], strng_lower.count(a[i])))

# =================================================================

import sys, string

s = []
for i in sys.stdin:
    s.append(i)

ss = ''.join(s).lower()

for char in string.ascii_lowercase:
    print("{} : {}".format(char, ss.count(char)))

