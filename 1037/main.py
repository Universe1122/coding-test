index = int(input())
data = sorted(list(map(int, input().split())))

print(data[0]*data[index-1])