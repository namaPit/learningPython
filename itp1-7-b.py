while True:
    n,x = map(int, input().split())
    if n == x == 0:
        break
    
    tmp = 0

    for i1 in range(0,n-1):
        for i2 in range(i1, n):
            n3 = x - i1 - i2
            if (n3 != i2)and(i2 != i1)and(0 < i1 < i2 < n3)and(0 < n3 <= n):
                tmp += 1
    
    print(tmp)

