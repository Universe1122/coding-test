data = []
for _ in range(3):
    data.append(list(map(int, input().split())))

index = 0
if data[0][0] == data[1][0]:
    index = 2
elif data[0][0] == data[2][0]:
    index = 1
else:
    index = 0

if data[0][1] == data[1][1]:
    print(data[index][0], data[2][1])
elif data[0][1] == data[2][1]:
    print(data[index][0], data[1][1])
else:
    print(data[index][0], data[0][1])