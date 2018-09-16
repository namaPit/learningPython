n=input()
ary=list(map(int, input().split()))
ary.sort()
print(ary[0],ary[-1],sum(ary))
