# 직사각형 네개의 합집합의 면적 구하기
import sys

input = sys.stdin.readline
board = [[0 for _ in range(101)] for _ in range(101)]
cnt = 0
for _ in range(4):
    x1, y1, x2, y2 = map(int, input().split())
    for y in range(y1, y2):
        for x in range(x1, x2):
            if board[y][x] != 1:
                board[y][x] = 1
                cnt += 1
print(cnt)
