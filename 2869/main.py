import sys
import math

A,B,V = map(int, sys.stdin.readline().split())

result = (V-B) / (A-B)
print(math.ceil(result))