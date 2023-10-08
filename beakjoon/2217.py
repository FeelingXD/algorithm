# 로프
import sys
from collections import deque
input = sys.stdin.readline

if __name__ == "__main__":
    ropes = []
    for _ in range(n := int(input())):
        ropes.append(int(input()))
    ropes.sort()
    dp = [0 for _ in range(n+1)]
    for i in range(len(ropes)):
        dp[i+1] = ropes[i]*(n-i)
    print(max(dp))
