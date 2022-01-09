data = input()
result = 0

if len(data) == 3:
    if data.find("0") == 1:
        a, b = map(int, data.split("0"))
        print(a*10 + b)
    else:
        print(int(data[0]) + int(data[1:]))
        
elif len(data) == 4:
    print(int(data[:2]) + int(data[2:]))

else:
    print(int(data[0]) + int(data[1]))