# 분산처리
import sys
from collections import deque
input = sys.stdin.readline

n = int(input())

for _ in '('*n:
    a, b = map(int, input().split())
    print(pow(a, b, 10) if pow(a, b, 10) != 0 else 10)
