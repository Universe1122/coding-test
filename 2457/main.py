import sys

flower_cnt = int(sys.stdin.readline())
flower_info = list()

for _ in range(flower_cnt):
    info = list(map(int, sys.stdin.readline().split(" ")))
    flower_info.append([info[0] * 100 + info[1], info[2] * 100 + info[3]])

max_date = 0
check = 0
count = 0
for info in flower_info:
    if info[0] <= 301:
        if max_date < info[1]:
            max_date = info[1]
            check = 1

if check:
    count += 1
else:
    print(0)
    exit()

while max_date < 1201:
    check = 0
    start_day = max_date
    for info in flower_info:
        if info[0] > 301 and info[0] <= start_day:
            if max_date < info[1]:
                max_date = info[1]
                check = 1
        
    if check:
        count += 1
    else:
        count = 0
        break

print(count)