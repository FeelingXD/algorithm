# 수 정렬하기 3
import sys
input = sys.stdin.readline

n = int(input())
l = []
tmp = [0]*10001

for _ in '_'*n:
    tmp[int(input())] += 1

for i in range(1, len(tmp)):
    if tmp[i] != 0:
        for j in range(tmp[i]):
            print(i)
