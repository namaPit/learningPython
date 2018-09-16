mark = ['S', 'H', 'C', 'D']
ary = []

for mk in range(0, 4):
    for i in range(1, 14):
        ary.append("{} {}".format(mark[mk], i))

n = int(input())
x = 0

while True:
    card = str(input())
    ary.remove(card)

    x += 1

    if x == n:
        break
    
if len(ary) > 0:
    print("\n".join(ary))


