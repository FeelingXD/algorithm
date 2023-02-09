# 스택
import sys
input = sys.stdin.readline
case = int(input())
stack = []
for _ in '*'*case:
    key = list(map(str, input().split()))
    if key[0] == 'push':
        stack.append(int(key[1]))
    elif key[0] == 'pop':
        print(stack.pop() if stack else -1)
    elif key[0] == 'size':
        print(len(stack))
    elif key[0] == 'empty':
        print(0 if stack else 1)
    elif key[0] == 'top':
        print(stack[-1] if stack else -1)
