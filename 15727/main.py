data = int(input())
count = 0

while data >= 5:
    data = data - 5
    count += 1

if data == 0:
    print(count)
else:
    print(count+1)