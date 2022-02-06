data = 1
result = []
for i in range(3):
    data *= int(input())

for i in range(10):
    result.append(str(str(data).count(str(i))))

print("\n".join(result))