# 색종이
import sys
input = sys.stdin.readline
papers = int(input())
maps = [[0]*101 for _ in range(101)]

cnt = 0
for _ in range(papers):
    valueX, valueY = map(int, input().split())
    for x in range(valueX, valueX+10):
        for y in range(valueY, valueY+10):
            if maps[x][y] == 0:
                cnt += 1
            maps[x][y] = 1
print(cnt)
