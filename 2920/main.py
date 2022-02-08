data = list(map(int, input().split()))
ascending = 0
descending = 0

for i in range(1, 8):
    if abs(data[i-1] - data[i]) != 1:
        print("mixed")
        exit()
    elif data[i-1] - data[i] == 1:
        ascending = 0
        descending = 1
    else:
        ascending = 1
        descending = 0

if ascending: print("ascending")
else: print("descending")