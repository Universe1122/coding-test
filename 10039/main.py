result = 0
for _ in range(5):
    tmp = int(input())

    if tmp < 40:
        tmp = 40
    
    result += tmp
print(result//5)