# 초콜릿 자르기
import sys
from collections import deque
input = sys.stdin.readline

if __name__ == "__main__":
    m, n = map(int, input().split())
    print(m*n-1)
