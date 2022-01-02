import datetime

result = []
for _ in range(3):
    data = list(map(int, input().split()))
    time_start =datetime.timedelta(hours=data[0], minutes=data[1], seconds=data[2])
    time_end = datetime.timedelta(hours=data[3], minutes=data[4], seconds=data[5])
    time = time_end - time_start

    result.append(str(time).replace(":", " ").replace("00", "0"))

print("\n".join(result))