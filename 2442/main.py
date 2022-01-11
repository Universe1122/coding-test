data = int(input())

for loop in range(1, data+1):
    result = ""
    result += " " * (data - loop)
    result += "*" * (2*loop - 1)

    print(result)