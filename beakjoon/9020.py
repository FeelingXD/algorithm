# 골드바흐의 추측
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


cases = int(input())
for i in range(cases):
    inputV = int(input())
    a, b = inputV//2, inputV//2
    while 0 < a:
        if isPrime(a) and isPrime(b):
            print(f'{a} {b}')
            break
        else:
            a -= 1
            b += 1
