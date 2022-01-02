a,b = map(int,input().split())

if a == b:
    print(a)
else:
    if a > b:
        c = a
        a = b
        b = c
    
    if (b - a) % 2 == 1:
        tmp = (b - a + 1) // 2
        result = (a + b) * tmp
    else:
        tmp = (b - a) // 2
        middle = (a + b) // 2
        result = (a + b) * tmp + middle
    
    print(result)