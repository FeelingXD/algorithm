# 리코쳇 로봇
from collections import deque

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]


def solution(board):
    goal, st = find_points(board)
    visited = [[False for _ in range(len(board[0]))]
               for _ in range(len(board))]
    answer = bfs(st, goal, board, visited)
    print(answer)
    return answer


def examine_edge(pos, board):
    y, x = pos
    if x == 0 or x == len(board[0]) or y == 0 or y == len(board):
        return True
    return False


def bfs(st, goal, board, visited):
    q = deque()
    q.append([st, 0])
    visited[st[0]][st[1]] = True

    while q:
        c_pos, depth = q.popleft()
        if c_pos == goal:
            return depth
        else:
            for i in range(4):
                ny, nx = c_pos
                while 0 <= nx+dx[i] < len(board[0]) and 0 <= ny+dy[i] < len(board):
                    # 엣지일경우 break

                    # d 이전일 경우 break
                    if board[ny+dy[i]][nx+dx[i]] == 'D':
                        break
                    nx += dx[i]
                    ny += dy[i]

                # todo q append
                if not visited[ny][nx]:
                    visited[ny][nx] = True
                    q.append([[ny, nx], depth+1])
    return -1
    pass


def find_points(board):
    goal = []
    st = []
    for y in range(len(board)):
        for x in range(len(board[0])):
            if board[y][x] == 'R':
                st = [y, x]
            if board[y][x] == 'G':
                goal = [y, x]
            if goal and st:
                return [goal, st]


solution(["...D..R", ".D.G...", "....D.D", "D....D.", "..D...."])
