N = int(input())
data = list(map(int, input().split()))

min = data[0]
max = data[0]

for i in data[1:]:
    if min > i:
        min = i
    elif max < i:
        max = i

print(min, max)