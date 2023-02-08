import sys
# 피보나치수 5
input = sys.stdin.readline
case = int(input())


def fibo(n):
    if n == 0:
        return 0
    elif n == 1 or n == 2:
        return 1
    else:
        return fibo(n-1)+fibo(n-2)


print(fibo(case))
