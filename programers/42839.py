# 소수 찾기
from itertools import permutations


def isPrime(num: int):
    if num < 2:
        return False
    elif num == 2:
        return True
    else:
        for i in range(2, int(num**(1/2))+1):
            if num % i == 0:
                return False
        return True


def solution(numbers):
    tmp = set()
    for i in range(1, len(numbers)+1):
        for j in permutations(numbers, i):
            value = int(''.join(j))
            tmp.add(value)
    return len([i for i in tmp if isPrime(i)])
