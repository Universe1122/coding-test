data = list(map(int, input().split()))
result = 0
for year in range(1, data[0]+1):
    result = result + ( data[1] * year + data[2] * year ** 2)

print(result)