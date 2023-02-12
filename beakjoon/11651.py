
# 좌표 정렬하기 2
import sys
input = sys.stdin.readline

case = int(input())

coordinates = []
for _ in range(case):
    coordinates.append(list(map(int, input().split())))
coordinates.sort(key=lambda x: (x[1], x[0]))


for i in coordinates:
    print(*i)
