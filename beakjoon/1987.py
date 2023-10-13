# 알파벳
import sys
from collections import deque
input = sys.stdin.readline
moves = [(0, 1), (0, -1), (-1, 0), (1, 0)]


def bfs():
    q = set()
    q.add((0, 0, maps[0][0]))
    ans = 0
    while q:
        y, x, l = q.pop()
        ans = max(ans, len(l))
        if ans == 26:
            return ans
        for move in moves:
            dy, dx = move
            ny, nx = dy+y, dx+x
            if 0 <= ny < r and 0 <= nx < c and maps[ny][nx] not in l:
                q.add((ny, nx, l+maps[ny][nx]))
    return ans


if __name__ == "__main__":
    r, c = map(int, input().split())
    maps = [input().strip() for _ in range(r)]
    print(bfs())
