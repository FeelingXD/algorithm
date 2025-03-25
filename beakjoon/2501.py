# 약수 구하기
import sys

input = sys.stdin.readline


def solution():
    n, k = map(int, input().split())

    numbers = get_measures(n)
    if k == 1:
        print(1)
        exit()
    print(numbers[k - 1] if len(numbers) >= k else 0)
    pass


def get_measures(n: int) -> list:

    result = [1, n]

    for i in range(2, int(n**0.5) + 1, 1):
        if n % i == 0:
            if i != n**0.5:
                result.append(i)
                result.append(n // i)
            else:
                result.append(int(n**0.5))

    return sorted(result)
    pass


if __name__ == "__main__":  # 실행되는 부분
    solution()
    pass
