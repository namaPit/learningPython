def non_minus(n):
    if n < 0:
        return (-1) * n
    else:
        return n

def kyori(n1, n2):
    n1 = non_minus(n1)
    n2 = non_minus(n2)
    n3 = non_minus(n1 - n2)
    return n3

def minkov(x: list, y: list, p: int):
    len_x = len(x)
    dm = 0
    for i in range(len_x):
        dm += kyori(x[i], y[i])**p
    dxy = dm**(1/p)
    return dxy

def chebyshev(x: list, y: list):
    d_ary = []
    len_x = len(x)
    for i in range(len_x):
        d_ary.append(kyori(x[i], y[i]))
    
    return max(d_ary)

n = int(input())
x = list(map(int, input().split()))
y = list(map(int, input().split()))

print(minkov(x,y,1))
print(minkov(x,y,2))
print(minkov(x,y,3))
print(float(chebyshev(x,y)))



