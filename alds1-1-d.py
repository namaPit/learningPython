def tansaku(ary: list):
    diff = -999999999999
    x = len(ary)
    for i in range(x):
        for j in range(x):
            if j > i:
                if diff < (ary[j]-ary[i]):
                    diff = (ary[j]-ary[i])
    
    return diff

n = int(input())
ary = []

for i in range(n):
    ary.append(int(input()))

ans = tansaku(ary)

print(ans)
