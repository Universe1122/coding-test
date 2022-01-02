cur = list(map(int, input().split()))
tmp = int(input())

cur[0] = (cur[0] + (cur[1] + tmp)//60) % 24
cur[1] = (cur[1] + tmp)%60
print(cur[0], cur[1])