data = []
for _ in range(3):
    data.append(int(input()))

if sum(data) != 180:
    print("Error")
elif data.count(60) == 3:
    print("Equilateral")
else:
    for d in data:
        if data.count(d) == 2:
            print("Isosceles")
            break
    else:
        print("Scalene")