# 수 정렬하기 4
import sys
input = sys.stdin.readline

case = int(input())

coordinates = []
for _ in range(case):
    coordinates.append(int(input()))
coordinates.sort(reverse=True)

for i in coordinates:
    print(i)
