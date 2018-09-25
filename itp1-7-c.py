r,c = map(int, input().split())
ary = []


for i in range(r):
    ary.append(list(map(int, input().split())))

# 最後に各列の合計を書き加えるための行を追加。
ary.append([0]*c)

# 合計を出すための一時データとして変数tmpを初期化
tmp = 0

# 各列の合計を求めて、最終行に加えた数値を書き換える
for i2 in range(c):
    for i1 in range(r):
        tmp += ary[i1][i2]
    ary[i1+1][i2] = tmp
    tmp = 0


# 各行の行末に、各行の合計をappendで追加

for i1 in range(r+1):
    for i2 in range(c):
        tmp += ary[i1][i2]
    ary[i1].append(tmp)
    tmp = 0

for i1 in range(r+1):
    print(" ".join(map(str, ary[i1])))


