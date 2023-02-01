# 소수만들기
from itertools import combinations


def isPrime(n):
    if n % 2 == 0 or n % 3 == 0:
        return False
    if n == 3:
        return True
    else:
        for i in range(5, n, 2):
            if n % i == 0:
                return False
        return True


def solution(nums):
    return len([i for i in list(combinations(nums, 3)) if isPrime(sum(i))])
