data = list(input().split("-"))
result = []

for i in range(len(data)):
    result.append(data[i][0])

print("".join(result))