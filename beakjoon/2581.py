
# 소수
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


start = int(input())
end = int(input())
minV = 0
tot = 0
for i in range(start, end+1):
    if isPrime(i):
        if not minV:
            minV = i
        tot += i
if tot:
    print(tot)
    print(minV)
else:
    print(-1)
