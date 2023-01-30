# 다리 놓기
import sys
import math
input = sys.stdin.readline

cases = int(input())
for _ in '('*cases:
    a, b = map(int, input().split())
    print((int)(math.factorial(b)/(math.factorial(b-a)*math.factorial(a))))
