N = int(input())
count = 0

for z in range(2, N+1):
    if z%2 != 0:
        continue

    tmp = N - z

    for a in range(1, tmp+1):
        if a + (a + 2) > tmp:
            break
        count += 1

print(count)