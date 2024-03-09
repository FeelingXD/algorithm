# 모음의 개수
import sys

input = sys.stdin.readline


def solution():
    word = input().strip()
    cnt = 0
    for c in word:
        if c in ("a", "e", "i", "o", "u"):
            cnt += 1
    print(cnt)
    pass


if __name__ == "__main__":  # 실행되는 부분
    solution()
    pass
