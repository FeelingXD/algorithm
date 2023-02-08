# 좌표 정렬하기
import sys
input = sys.stdin.readline


case = int(input())
positions = []
for i in range(case):
    x, y = map(int, input().split())
    positions.append((x, y))
positions.sort(key=lambda x: (x[0], x[1]))
for i in positions:
    print(i[0], i[1])
