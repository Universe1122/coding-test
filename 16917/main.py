A,B,C,X,Y = map(int, input().split())
min_money = A*X + B*Y

count = max(X,Y)

for i in range(1, count+1):
    result = C * i * 2
    result += A * max(0, (X - i))
    result += B * max(0, (Y - i))

    if min_money > result:
        min_money = result

print(min_money)