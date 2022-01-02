h,m,s = map(int, input().split())
tmp = int(input())

s = s + tmp
m = m + s//60
h = (h + (m//60))%24
m = m%60
s = s%60

print(h, m ,s)