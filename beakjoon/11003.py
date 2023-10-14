# 최솟값 찾기
import sys
from collections import deque
input = sys.stdin.readline

if __name__ == "__main__":
    n, l = map(int, input().split())
    D = list(map(int, input().split()))
    q = deque()
    for i in range(n):
        if q and q[0][0] <= i-l:
            q.popleft()

        while q and D[i] < q[-1][1]:
            q.pop()

        q.append((i, D[i]))
        print(q[0][1], end=" ")
