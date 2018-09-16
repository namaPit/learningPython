a,b,c = [int(i) for i in input().split()]

num=a
ans=0
while True:
    if c%num == 0:
        ans+=1
    
    num+=1

    if num > b:
        break
    

print(ans)
