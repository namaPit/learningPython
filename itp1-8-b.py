while True:
    a = input()
    if a == '0':
        break
    
    sum = 0

    for i in range(len(a)):
        sum += int(a[i])
    
    print(sum)
    