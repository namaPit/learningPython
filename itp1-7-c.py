r,c = map(int, input().split())
ary = []


for i in range(r):
    ary.append(list(map(int, input().split())))

ary.append([0]*c)



for i1 in range(r+1):
    for i2 in range(c+1):
        print(" %d"%(ary[i1][i2]), end = "")
    print("")

