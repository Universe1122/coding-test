import datetime

data = list(map(int, input().split()))
time = datetime.datetime(2022,1,1,data[0], data[1], 0)
result = time - datetime.timedelta(minutes=45)
print(result.hour, result.minute)