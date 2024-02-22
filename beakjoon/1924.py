# 2007년
import sys

input = sys.stdin.readline

MONTH = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
DAY = ["SUN", "MON", "TUE", "WED", "THU", "FRI", "SAT"]


def solution():
    m, d = map(int, input().split())
    t = 0
    for i in range(m - 1):
        t += MONTH[i]
    print(DAY[(t + d) % 7])
    pass


if __name__ == "__main__":  # 실행되는 부분
    solution()
    pass
