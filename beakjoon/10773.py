# 제로
import sys
input = sys.stdin.readline

stack = []
for i in range(int(input())):
    i = int(input())
    if i == 0:
        stack.pop()
    else:
        stack.append(i)
print(sum(stack))
