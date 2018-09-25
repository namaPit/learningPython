w = input().lower()
ans = 0
while True:
    tmp = input()
    if tmp =="END_OF_TEXT":
        break
    tmp = tmp.lower().split()
    ans += tmp.count(w)


print(ans)
