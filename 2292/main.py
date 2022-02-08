data = int(input())

if data == 1:
    print(1)
elif data <=7:
    print(2)
else:
    min = 2
    degree = 5
    for i in range(1, 10000000000000):
        min += 6 * i
        degree += 6

        if data >= min and data <= min + degree:
            print(i+2)
            break