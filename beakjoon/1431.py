# 시리얼 번호
import sys
from collections import deque
input = sys.stdin.readline

if __name__ == "__main__":
    n = int(input())
    serials = []
    for _ in range(n):
        nv = 0
        v = input().strip()
        for c in v:
            if c.isdigit():
                nv += int(c)
        serials.append((v, len(v), nv))
    serials.sort(key=lambda x: (x[1], x[2], x[0]))
    for serial in serials:
        print(serial[0])
