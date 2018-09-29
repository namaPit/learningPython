def euc_core(a,b):
    mod = a % b

    return b, mod

def euc(a,b):
    a_i = a
    b_i = b
    while True:
        if b_i == 0:
            break
        a_i, b_i = euc_core(a_i, b_i)
    
    return a_i


a,b = map(int, input().split())

if a < b :
    ai = a
    a = b
    b = ai

print(euc(a,b))
