# 단어 나누기
import sys

input = sys.stdin.readline


def solution():
    word = input().strip()
    l, r = 0, len(word) - 1
    candidate = []
    for l in range(1, len(word)):
        for r in range(l + 1, len(word)):
            candidate.append(word[:l][::-1] + word[l:r][::-1] + word[r:][::-1])
    candidate.sort()
    print(candidate[0])
    pass


if __name__ == "__main__":  # 실행되는 부분
    solution()
    pass
