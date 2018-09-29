s = str(input())
n = int(input())
m = []

for i in range(n):
    m = list(input().split())
    i1 = int(m[1])
    i2 = int(m[2])+1
    if m[0] == "replace":
        s = s[0:i1] + m[3] + s[i2::]
        # print(s)
    elif m[0] == "reverse":
        sr = s[i1:i2]
        sr = sr[::-1]
        s = s[0:i1] + sr + s[i2::]
        # print(s)
    elif m[0] == "print":
        print(s[i1:i2])

