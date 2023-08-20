# 소수 & 펠린드롬
import sys
input = sys.stdin.readline


def is_prime(n):
    if n == 1:
        return False
    elif n in (2, 3):
        return True
    elif n % 2 == 0:
        return False
    else:
        for i in range(3, int(n**(1/2)+1), 2):
            if n % i == 0:
                return False
    return True


def is_palindrome(n):
    return True if str(n) == str(n)[::-1] else False


n = int(input())

while True:
    if is_prime(n) and is_palindrome(n):
        print(n)
        break
    n += 1
