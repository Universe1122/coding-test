N = int(input())
data = list(map(int, input().split()))
count = 0

for i in range(1, N+1):
    if i != data[i-1]:
        count += 1

print(count)