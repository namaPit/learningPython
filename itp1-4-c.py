while True:
    a,op,b = input().split()

    a = int(a)
    b = int(b)

    if op == '?':
        break
    elif op == '+':
        print(a+b)
    elif op == '-':
        print(a-b)
    elif op == '*':
        print(a*b)
    elif op == '/':
        print(a/b)
    




while True:
    s=input()
    if '?' in s:
        break
    
    print(int(eval(s)))
    