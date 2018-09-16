while True:
    h,w = map(int, input().split())
    if w==0 and h==0:
        break
    
    s = '#'
    for prt in range(h):
        print(s*w)
    
    print()


