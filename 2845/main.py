import sys

input_1 = list(map(int, sys.stdin.readline().split(" ")))
input_2 = list(map(int, sys.stdin.readline().split(" ")))

data = input_1[0] * input_1[1]
result = []

for d in input_2:
    result.append(str(d - data))
print(" ".join(result))