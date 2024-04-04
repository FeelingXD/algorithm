# 분수찾기
import sys

input = sys.stdin.readline


def solution():
    n = int(input())
    line, end = 0, 0

    while n > end:
        line += 1
        end += line
    diff = end - n
    # print(f"{end=}")
    if line % 2:  # line이 홀수 번일때
        top = diff + 1
        bottom = line - diff
    else:  # 짝수일때
        top = line - diff
        bottom = diff + 1
    print(f"{top}/{bottom}")
    pass


if __name__ == "__main__":  # 실행되는 부분
    solution()
    pass
