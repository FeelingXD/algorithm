import sys
input = sys.stdin.readline


def is_prime(n):
    if n == 2 or n == 3:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, n, 2):
        if n % i == 0:
            return False
    return True


n = int(input())
values = list(map(int, input().split()))
print(len(set([i for i in range(2, max(values)+1) if is_prime(i)]) & set(values)))
