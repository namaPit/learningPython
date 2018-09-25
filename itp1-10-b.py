import math
a,b,c = map(float, input().split())
s = a * b * math.sin(math.radians(c)) / 2
l = math.sqrt(a**2+b**2-2*a*b*math.cos(math.radians(c)))+a+b
h = s * 2 / a

print(s)
print(l)
print(h)
