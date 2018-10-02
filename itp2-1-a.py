n = int(input())
a = []

for i in range(n):
    d = list(map(int, input().split()))
    if d[0] == 0:
        a.append(d[1])
    elif d[0] == 1:
        print(a[d[1]])
    elif d[0] == 2:
        a.pop()

