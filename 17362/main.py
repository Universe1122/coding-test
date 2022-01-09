data = int(input()) % 8

if data == 1: print(1)
elif data == 2 or data == 0: print(2)
elif data == 3 or data == 7: print(3)
elif data == 4 or data == 6: print(4)
else: print(5)