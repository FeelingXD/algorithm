# 전자레인지
import sys

input = sys.stdin.readline


if __name__ == "__main__":
    n = int(input())
    answer = []
    T = [300, 60, 10]
    for t in T:
        answer.append(n//t)
        n %= t
    print(' '.join(map(str, answer)) if n == 0 else -1)

    pass
