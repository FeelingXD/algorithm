# 분해합
import sys
input = sys.stdin.readline
num = int(input())

for i in range(1, num+1):
    num_sum = sum(map(int, str(i)))
    tot = num_sum+i
    if tot == num:
        print(i)
        break
    elif i == num:
        print(0)
