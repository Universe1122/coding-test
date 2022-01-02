data = []
for _ in range(5):
    data.append(int(input()))

first = data[0] * data[4]
if data[2] < data[4]:
    result = data[1] + (data[4] - data[2]) * data[3]
else:
    result = data[1]

if result < first:
    print(result)
else:
    print(first)