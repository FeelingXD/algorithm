# 최댓값
import sys
input = sys.stdin.readline

maxV = float('-inf')
x, y = 0, 0
for i in range(9):
    li = list(map(int, input().split()))
    if max(li) > maxV:
        y = li.index(max(li))+1
        x = i+1
        maxV = max(li)

print(maxV)
print(f'{x} {y}')
