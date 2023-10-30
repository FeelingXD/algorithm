# 주유소
import sys
from collections import deque
input = sys.stdin.readline
if __name__ == "__main__":
    n = int(input())
    lines = deque(list(map(int, input().split())))
    prices = deque(list(map(int, input().split())))
    c_p = prices.popleft()
    answer = c_p * lines.popleft()
    while lines:
        c_p = min(c_p, prices.popleft())
        c_l = lines.popleft()
        answer += c_p*c_l
    print(answer)
    pass
