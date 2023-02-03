# 색종이 만들기
import sys
input = sys.stdin.readline


case = int(input())
maps = [list(map(int, input().split())) for _ in range(case)]

white = 0
blue = 0


def dq(maps, x, y, l):  # x y l
    global white, blue
    tmp = maps[x][y]
    for i in range(x, x+l):
        for j in range(y, y+l):
            if maps[i][j] != tmp:
                dq(maps, x, y, l // 2)
                dq(maps, x + l // 2, y, l // 2)
                dq(maps, x, y + l // 2, l // 2)
                dq(maps, x + l // 2, y + l // 2, l // 2)
                return
    if not tmp:
        blue += 1
    else:
        white += 1


dq(maps, 0, 0, case)
print(blue)
print(white)
