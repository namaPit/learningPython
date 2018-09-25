n,m,l = map(int, input().split())
a = []
b = []
c = []

for i1 in range(n):
    a.append(list(map(int, input().split())))

for i2 in range(m):
    b.append(list(map(int,input().split())))

for i1 in range(n):
    c.append([0]*l)

for i1 in range(n):
    for i3 in range(l):
        for i2 in range(m):
            c[i1][i3] += a[i1][i2] * b[i2][i3]

for i1 in range(n):
    print(" ".join(map(str, c[i1])))

