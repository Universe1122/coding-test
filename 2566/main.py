data = []
for _ in range(9):
    data.append(list(map(int, input().split())))

max = data[0][0]
x = 0
y = 0

for i in range(9):
    for j in range(9):
        if max < data[i][j]:
            max = data[i][j]
            x = i
            y = j

print(max)
print(x+1, y+1)