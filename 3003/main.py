import sys

data = list(map(int, sys.stdin.readline().split(" ")))
init = [1, 1, 2, 2, 2, 8]
result = []

for index in range(len(data)):
    result.append(str(init[index] - data[index]))

print(" ".join(result))