# 경주로 건설
from collections import deque
inf = 10e8
moves = [(0, 1), (0, -1), (1, 0), (-1, 0)]
WALL = 1
PATH = 0


def bfs(board):

    lr, lc = len(board), len(board[0])
    visited = [[[inf]*4 for _ in range(lc)] for _ in range(lr)]
    for i in range(4):
        visited[0][0][i] = 0

    q = deque()
    # 이전 방향정보 와 좌표 기록
    q.append(((0, 0), 0))  # 우측으로 가는경우
    q.append(((0, 0), 2))  # 아래로 가는경우
    while q:
        c_pos, past_d = q.popleft()
        cy, cx = c_pos
        for i in range(4):
            dy, dx = moves[i]
            ny, nx = dy+cy, dx+cx
            c_cost = 100 if i == past_d else 600  # 이전과 방향같을경우 직진
            if 0 <= ny < lr and 0 <= nx < lc and board[ny][nx] != WALL and visited[ny][nx][i] > visited[cy][cx][past_d]+c_cost:
                visited[ny][nx][i] = visited[cy][cx][past_d]+c_cost
                q.append(((ny, nx), i))
    return min(visited[-1][-1])


def solution(board):
    return bfs(board)
