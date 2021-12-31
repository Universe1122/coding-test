data = []
for _ in range(5):
    data.append(int(input()))

min = data[0] + data[3]
for i in range(3):
    for j in range(3, 5):
        tmp = data[i] + data[j]

        if min > tmp:
            min = tmp
    
print(min-50)