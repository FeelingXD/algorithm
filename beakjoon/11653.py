# 소인수 분해
import sys
input = sys.stdin.readline
num = int(input())

for i in range(2, num+1):
    while num % i == 0:
        print(i)
        num //= i
    if num == 1:
        break
