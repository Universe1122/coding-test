data1 = list(map(int, input().split()))
data2 = list(map(int, input().split()))

a = data1[0] + data2[1]
b = data1[1] + data2[0]
if a < b:
    print(a)
else:
    print(b)