# 국영수
import sys

input = sys.stdin.readline


def seperate(word):
    name, lang_score, eng_score, math_score = word.split()
    return (name, int(lang_score), int(eng_score), int(math_score))


def solution():
    N = int(input())
    students = []
    for _ in range(N):
        students.append(seperate(input().strip()))
    students.sort(key=lambda x: (-x[1], x[2], -x[3], x[0]))
    for name, *_ in students:
        print(name)
    pass


if __name__ == "__main__":  # 실행되는 부분
    solution()
    pass
