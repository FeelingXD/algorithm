# 문서검색
import sys

input = sys.stdin.readline


if __name__ == "__main__":
    word = input().strip()
    target = input().strip()
    print(word.count(target))
    pass
