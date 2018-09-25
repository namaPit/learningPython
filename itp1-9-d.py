s = str(input())
n = int(input())
m = []

for i in range(n):
    m = list(input().split())
    i1 = int(m[1])
    i2 = int(m[2])+1
    if m[0] == "replace":
        s = s[0:i1] + m[3] + s[i2::]
        print(s)
    elif m[0] == "reverse":
        i11 = -1 * i1
        i21 = -1 * i2
        sr = s[::-1]
        print(sr[i21:i11])
        s = s[0:i1] + sr[i21:i11] + s[i2::]
        print(s)
    elif m[0] == "print":
        print(s[i1:i2])

