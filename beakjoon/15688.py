# 수 정렬하기 5
import sys
input = sys.stdin.readline

case = int(input())

coordinates = []
for _ in range(case):
    coordinates.append(int(input()))
coordinates.sort()

for i in coordinates:
    print(i)
