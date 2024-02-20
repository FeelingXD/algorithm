# 회문
import sys

input = sys.stdin.readline


def check(l, r, word):
    while l < r:
        if word[l] == word[r]:
            l += 1
            r -= 1
        else:
            # 우측 문자 를 제거하는경우
            if (tmp := word[:r] + word[r + 1 :]) and tmp == tmp[::-1]:
                return 1
                pass
            # 좌측 문자를 제거하는경우
            if (tmp := word[:l] + word[l + 1 :]) and tmp == tmp[::-1]:
                return 1
            return 2
    return 0


def solution():
    for _ in range(case := int(input())):
        word = input().strip()
        l, r = 0, len(word) - 1
        print(check(l, r, word))
    pass


if __name__ == "__main__":  # 실행되는 부분
    solution()
    pass
