# 진법 변환
import sys

input = sys.stdin.readline
DIFF = 55


def conversion(n, word):  # n 진수 -> 10진수 변환
    ans = 0
    for i, v in enumerate(word[::-1]):
        if "A" <= v:
            ans += (ord(v) - DIFF) * n**i
        else:
            ans += (int(v)) * n**i
    return ans


def solution():
    word, n = input().split()
    print(conversion(int(n), word))
    pass


if __name__ == "__main__":  # 실행되는 부분
    solution()
    pass
