import sys

result = 0
for _ in range(4):
    sec = int(sys.stdin.readline())
    result += sec

print(int(result / 60))
print(result % 60)