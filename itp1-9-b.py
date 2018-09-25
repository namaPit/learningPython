while True:
    s = input()
    if s == "-":
        break
    m = int(input())
    l = len(s)
    for i in range(m):
        h = int(input())
        s = s[h:l]+s[0:h]
    print(s)
