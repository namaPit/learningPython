W,H,x,y,r = [int(i) for i in input().split()]

flg = 0

# はみ出る条件に当てはまったらflgを増やす
if x<r:
    flg+=1

if y<r:
    flg+=1

if W-r<x:
    flg+=1

if H-r<y:
    flg+=1


# flgが0なら、はみ出る条件に当てはまってない。
if flg==0:
    print("Yes")
else:
    print("No")

