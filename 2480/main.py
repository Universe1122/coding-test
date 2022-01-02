data = list(map(int, input().split()))
data.sort()

if data.count(data[2]) == 3:
    print(10000 + data[2] * 1000)
elif data.count(data[1]) == 2:
    print(1000 + data[1] * 100)
else:
    print(100 * data[2])