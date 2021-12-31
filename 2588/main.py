data = []
for _ in range(2):
    data.append(int(input()))

print(data[0]*(data[1]%10))
print(data[0]*(data[1]%100 - data[1]%10)//10)
print(data[0]*(data[1]//100))
print(data[0]*data[1])