data = input()
previous = ""
result = 0

for d in data:
    if d == "(":
        if d == previous:
            result += 5
        else:
            result += 10
    else:
        if d == previous:
            result += 5
        else:
            result += 10
    
    previous = d
print(result)