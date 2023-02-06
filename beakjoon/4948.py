# 베르트랑 공준
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


n = 1
while n:
    n = int(input())
    cnt = 0
    if n == 0:
        break
    for i in range(n+1, 2*n+1):
        if isPrime(i):
            cnt += 1
    print(cnt)
