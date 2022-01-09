N, X = map(int, input().split())
data = list(map(int, input().split()))
result = []

for i in range(N):
    if data[i] < X:
        result.append(str(data[i]))

print(" ".join(result))