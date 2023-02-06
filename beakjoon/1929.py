# 소수 구하기
import sys
import math
input = sys.stdin.readline


def isPrime(n):
    if n == 2 or n == 3:
        return True
    if n % 2 == 0 or n % 3 == 0 or n == 1:
        return False
    for i in range(5, int(math.sqrt(n))+1, 2):
        if n % i == 0:
            return False
    return True


str, end = map(int, input().split())
for i in range(str, end+1):
    if isPrime(i):
        print(i)
