loop = int(input())

for _ in range(loop):
    a, b = map(int, input().split())

    result = a

    if b != 1:
        for _ in range(b-1):
            result = result * a % 10

    if result % 10 == 0:
        print(10)
    else:
        print(result % 10)