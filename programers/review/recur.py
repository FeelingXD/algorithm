
from collections import deque


def solution(n, i, j):
    maps = [[0]*n for i in range(n)]
    lenm = len(maps)

    # 점화
    maps[0][lenm-1] = 1

    bfs(maps, 0, len(maps)-1)
    # print

    return maps[i][j]


def bfs(maps, x, y):
    queue = deque()
    n = int((y+1)//2)
    queue.append((x, y, n))

    while queue:
        x, y, n = queue.popleft()

        while n >= 1:
            if n != 1:
                plusV = (int(n**2))
                maps[x][(y)-n] = maps[x][(y)]+plusV
                maps[x+n][(y)-n] = maps[x][(y)-n]+plusV
                maps[x+n][(y)] = maps[x+n][(y)-n]+plusV

            if n == 1:
                maps[x][(y)-n] = maps[x][(y)]+1
                maps[x+n][(y)-n] = maps[x][(y)-n]+1
                maps[x+n][(y)] = maps[x+n][(y)-n]+1
                break

            queue.append((x, y-n, n//2))
            queue.append((x+n, y-n, n//2))
            queue.append((x+n, y, n//2))

            n //= 2


solution(4, 1, 3)
print("🐍 File: CodingTest/#test.py | Line: 47 | undefined ~ solution(4, 1, 3)",
      solution(4, 1, 3))
solution(8, 3, 6)
print("🐍 File: CodingTest/#test.py | Line: 50 | undefined ~ solution(8, 3, 6)",
      solution(8, 3, 6))
