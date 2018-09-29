from statistics import mean, median, variance, stdev

while True:
    n = int(input())
    if n == 0:
        break
    
    data = list(map(int, input().split()))

    stdev_data = stdev(data)

    print(stdev_data)
    