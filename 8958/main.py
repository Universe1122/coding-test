loop = int(input())
for _ in range(loop):
    data = input()
    result = 0
    count = 1

    for i in range(len(data)):
        if data[i] == "O":
            result += count
            count += 1
        else:
            count = 1
        
    print(result)