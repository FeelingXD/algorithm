# 1이 될때까지
import sys

number, divnumber = map(int, sys.stdin.readline().split())


def solution(n: int) -> int:
    answer = 0
    while n != 1:
        if n % divnumber == 0:
            n = n//divnumber
        else:
            n -= 1
        answer += 1
    return answer


solution(number)
print("🐍 File: Greedy/to_one.py | Line: 19 | undefined ~ solution(number)", solution(number))
