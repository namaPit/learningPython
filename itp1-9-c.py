n = int(input())
taro = 0
hana = 0
s=[]
ss=[]

for i in range(n):
    s = list(map(str, input().split()))
    # print(s)
    ss = sorted(s)
    # print(ss)

    if s[0] == s[1]:
        taro += 1
        hana += 1
    elif s == ss:
        hana += 3
    else:
        taro += 3
    

print("{} {}".format(taro, hana))

