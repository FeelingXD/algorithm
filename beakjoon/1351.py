# 무한수열
import sys
from collections import defaultdict
input = sys.stdin.readline


def dfs(n):
    if d[n] != 0:
        return d[n]
    else:
        d[n] = dfs(n//p) + dfs(n//q)
        return d[n]


if __name__ == "__main__":
    n, p, q = map(int, input().split())
    d = defaultdict(int)
    d[0] = 1
    print(dfs(n))
