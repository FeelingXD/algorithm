# 뱀과 사다리 게임

import sys
from collections import deque, defaultdict

input = sys.stdin.readline


def solution():
    global visited, board, snake_and_stair
    N, M = map(int, input().split())
    visited = [False] * 101
    board = [0] * 101
    snake_and_stair = defaultdict(
        int, {k: v for k, v in (map(int, input().split()) for _ in range(N + M))}
    )
    bfs(1)
    pass


def bfs(pos):
    q = deque([pos])
    visited[pos] = True  # 방문 여부를 저장
    board[pos] = 0  # 주사위 횟수를 저장
    while q:
        pos = q.popleft()
        if pos == 100:
            print(board[pos])
            break
        else:
            for dice in range(1, 7):
                next_pos = pos + dice
                if next_pos > 100 or visited[next_pos]:  # 방문 한경우 넘기기
                    continue
                if snake_and_stair[next_pos]:
                    next_pos = snake_and_stair[next_pos]  # 뱀,사다리 이동
                if visited[next_pos]:
                    continue
                board[next_pos] = board[pos] + 1
                visited[next_pos] = True
                q.append(next_pos)

                pass


if __name__ == "__main__":  # 실행되는 부분
    solution()
    pass
"""
2 2
3 99
10 44
99 10
44 19
"""
