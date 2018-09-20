# 各評定のボーダー値を定義
border_a = 80
border_b = 65
border_c = 50
border_d = 30
border_retest = 50

# 特定の入力値(-1, -1, -1)以外の間は繰り返す
while True:
    m,f,r = map(int, input().split())
    mf = m + f

    if (m==-1)and(f==-1)and(r==-1):
        break
    elif (m==-1)or(f==-1):
        print("F")
    elif mf >= border_a:
        print("A")
    elif mf >= border_b:
        print("B")
    elif mf >= border_c:
        print("C")
    elif mf >= border_d:
        if r >= border_retest:
            print("C")
        else:
            print("D")
    else:
        print("F")


