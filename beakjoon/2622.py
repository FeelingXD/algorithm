# 삼각형만들기
import sys
from math import ceil

input = sys.stdin.readline


def solution():
    matches = int(input())  # 성냥의 총길이
    """
        삼각형의 변 a,b,c 로 두었을때 
        - 삼각형의 성립조건 a+b>c 여야한다. (c 변이 가장 긴 변)
    """
    ans = 0
    for a in range(1, matches):
        for b in range(a, matches):
            c = matches - a - b
            if c >= a + b:
                continue
            if c < b:
                break
            if b + a > c:
                ans += 1
    print(ans)

    pass


if __name__ == "__main__":  # 실행되는 부분
    solution()
    pass
