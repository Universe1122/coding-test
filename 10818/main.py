N = int(input())
data = list(map(int, input().split()))

if N == 1:
    print(data[0])
elif N == 2:
    if data[0] > data[1]:
        print(data[1], data[0])
    else:
        print(data[0], data[1])

else:
    if data[0] > data[1]:
        max = data[0]
        min = data[1]
    else:
        max = data[1]
        min = data[0]

    for i in range(2, N):
        if max < data[i]:
            max = data[i]
        elif min > data[i]:
            min = data[i]

    print(min, max)