# 소수 찾기
import math


def solution(n):
    answer = 0
    for i in range(1, n+1):
        if isPrime(i):
            answer += 1

    return answer


def isPrime(n):
    if n == 1:
        return False
    elif n == 2:
        return True
    elif n % 2 == 0:
        return False
    else:
        for i in range(3, int(math.sqrt(n))+1):
            if n % i == 0:
                return False
        return True
