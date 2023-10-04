# 화살표 미로
import sys
from collections import deque
input = sys.stdin.readline
moves = [(0, -1), (1, 0), (0, 1), (-1, 0)]  # 0~ 상우하좌
dic = {'U': 0, 'R': 1, 'D': 2, 'L': 3}  # +90 도 회전


def drawboard(r):  # board 그리기
    board = []
    for _ in range(r):
        board.append(input().strip())
    return board


def bfs(r, c, k):
    board = drawboard(r)
    q = deque()
    if k == 0:  # k==0  방향회전하지 못하는경우
        visited = [[False]*c for _ in range(r)]
        visited[0][0] = 1
        q.append([0, 0])
        while q:
            y, x = q.popleft()
            dx, dy = moves[dic[board[y][x]]]
            ny, nx = y+dy, x+dx
            if 0 <= ny < r and 0 <= nx < c and not visited[ny][nx]:
                visited[ny][nx] = 1
                q.append([ny, nx])
        return 'Yes' if visited[-1][-1] else 'No'
    else:  # k==1 방향회전 가능한경우 이때 k 최대값은 1
        visited = [[[False]*4 for _ in range(c)] for _ in range(r)]
        q.append([0, 0, 0])
        visited[0][0][0] = 1

        while q:
            y, x, k = q.popleft()
            dx, dy = moves[dic[board[y][x]]]
            ny, nx = dy+y, dx+x
            if 0 <= ny < r and 0 <= nx < c and not visited[ny][nx][k]:
                visited[ny][nx][k] = 1
                q.append([ny, nx, k])
            if k & 1 == 0:  # 좌
                nk = k | 1
                dx, dy = moves[(dic[board[y][x]]-1) % 4]
                ny, nx = dy+y, dx+x
                if 0 <= ny < r and 0 <= nx < c and not visited[ny][nx][nk]:
                    visited[ny][nx][nk] = 1
                    q.append([ny, nx, nk])
            if k & 2 == 0:  # 우
                nk = k | 2
                dx, dy = moves[(dic[board[y][x]]+1) % 4]
                ny, nx = dy+y, dx+x
                if 0 <= ny < r and 0 <= nx < c and not visited[ny][nx][nk]:
                    visited[ny][nx][nk] = 1
                    q.append([ny, nx, nk])
        return 'No' if set(visited[-1][-1]) == {False} else 'Yes'

        pass
    pass


if __name__ == "__main__":
    r, c, k = map(int, input().split())
    print(bfs(r, c, k))
