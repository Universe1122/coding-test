import math

data = []
for _ in range(5):
    data.append(int(input()))

i = math.ceil(data[1] / data[3])
j = math.ceil(data[2] / data[4])

if i<j: print(data[0] - j)
else: print(data[0] - i)