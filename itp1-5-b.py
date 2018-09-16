while True:
    h,w = map(int, input().split())
    if w==0 and h==0:
        break
    
    s = '#'
    d = '.'

    for i in range(h):
        if i==0 or i==h-1:
            print(s*w)
        else:
            print(s+(d*(w-2))+s)
    
    print()

    
