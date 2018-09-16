while True:
    h,w = map(int, input().split())
    if w==0 and h==0:
        break
    
    s = '#'
    d = '.'

    str = ''

    for i1 in range(h):
        if i1%2 == 0:
            for i2 in range(w):
                if i2%2 == 0:
                    str = str + s
                else:
                    str = str + d
            
            print(str)
            str=''

        else:
            for i2 in range(w):
                if i2%2 == 0:
                    str = str + d
                else:
                    str = str + s
            
            print(str)
            str=''
    
    print()

    
