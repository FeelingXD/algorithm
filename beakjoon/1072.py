# 게임
import sys
import math
input = sys.stdin.readline

X, Y = map(int, input().split())
Z = Y*100//X
if Z >= 99:
    print(-1)
    exit()
else:
    answer = 0
    left = 1
    right = X
    mid = 0
    while (left <= right):
        mid = (left+right)//2
        if int((Y+mid)*100//(X+mid)) <= Z:
            left = mid+1
        else:
            answer = mid
            right = mid-1
    print(answer)
