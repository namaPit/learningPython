# n,mを取得
n,m = map(int, input().split())

# 配列a,bを初期化
a = [[] for i in range (0,n)]
b = [[0]*1 for i in range (0,m)]

for i1 in range(n):
    a[i1] = list(map(int, input().split()))

for i2 in range(m):
    b[i2] = int(input())

# 戻り値の各要素を個々に計算し、戻り値tmpの要素に加える
for i4 in range(n):
    tmp = 0
    for i5 in range(m):
        tmp += a[i4][i5]*b[i5]
    print(tmp)


