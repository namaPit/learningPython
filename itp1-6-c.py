n_room = 10     # 1フロアの部屋の数
n_floor = 3     # 1棟ごとの階数
n_blds = 4      # 棟の数

ary_r = []      # 部屋ごとの配列作成用
ary_f = []      # 階ごとの配列作成用
ary_b = []      # 全体の配列

for bld in range(1, n_blds + 1):
    for flr in range(1, n_floor + 1):
        for rm in range(1, n_room + 1):
            ary_r = ary_r.append(0)     # 各部屋の要素として初期値0を入れる
        
        ary_f = ary_f.append(ary_r)     # 各階ごとまとめて配列を複合化
        ary_r = []  # 配列を初期化
    
    ary_b = ary_b.append(ary_f)
    ary_f = []

n = int(input())
x = 0

while True:
    b,f,r,v = map(int, input().split())
    ary_b[b-1][f-1][r-1] += v


# あとは書き出すための部分を書く。

# =========================================================================

n_room = 10     # 1フロアの部屋の数
n_floor = 3     # 1棟ごとの階数
n_blds = 4      # 棟の数
cnt1 = 0           # 配列作成時のカウンタ


while True:
    ary[cnt1] = [[0] * n_room for i in range(n_floor)]
    cnt1+=1
    if cnt1 == n_blds:
        break
    

n = int(input())    # データ数を取得
cnt2 = 0            # データ取得用カウンタの初期化

while True:
    b,f,r,v = map(int, input().split())
    ary[b-1][f-1][r-1] += v
    cnt2 += 1
    if cnt2 == n:
        break
    

cnt_b = 0       # 棟を回すためのカウンタ
cnt_f = 0       # 階を回すためのカウンタ

