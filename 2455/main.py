in_train_count = 0
max = 0
for _ in range(4):
    data = list(map(int, input().split()))
    in_train_count += data[1] - data[0]

    if max < in_train_count:
        max = in_train_count

print(max)