# 문자열 폭팔
import sys
input = sys.stdin.readline
S = input().rstrip()
es = input().rstrip()

stack = []
for i in range(len(S)):
    stack.append(S[i])
    if ''.join(stack[-len(es):]) == es:
        for _ in range(len(es)):
            stack.pop()
print(''.join(stack) if stack else 'FRULA')
