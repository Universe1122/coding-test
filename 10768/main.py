data = []
for _ in range(2):
    data.append(int(input()))

tmp = data[0] * 100 + data[1]

if tmp == 218:
    print("Special")
elif tmp > 218:
    print("After")
else:
    print("Before")