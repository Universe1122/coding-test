data = []
result = []
for _ in range(3):
    data.append(list(map(int, input().split())))

for i in range(3):
    if data[i][0] * 10 >= 5000 :
        result.append(data[i][1] * 10 / (data[i][0] * 10 - 500))
    else:
        result.append(data[i][1] * 10 / data[i][0] * 10)
    
if max(result) == result[0]:
    print("S")
elif max(result) == result[1]:
    print("N")
else:
    print("U")