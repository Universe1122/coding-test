date = int(input())
car = list(map(int, input().split()))

count = 0
for d in car:
    if date == d:
        count += 1

print(count)