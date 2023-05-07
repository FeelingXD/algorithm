# 직각삼각형
import sys
from collections import deque
input = sys.stdin.readline

while True:
    edges = list(map(int, input().split()))
    edges.sort()
    if edges[0] == edges[1] == edges[2] == 0:
        break
    print("right" if (edges[0]**2+edges[1]**2) == (edges[2]**2) else 'wrong')
