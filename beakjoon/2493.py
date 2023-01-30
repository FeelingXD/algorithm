# 탑
from collections import deque
import sys
input = sys.stdin.readline


cases = int(input())
towers = list(map(int, input().split()))

stack = []
answer = [0]*len(towers)
tmp = towers[::-1]
for i in range(len(towers)):
    while stack and tmp[stack[-1]] < tmp[i]:
        answer[stack.pop()] = len(tmp)-i
    stack.append(i)
while stack:
    answer[stack.pop()] = 0
print(" ".join([str(i) for i in answer[::-1]]))
