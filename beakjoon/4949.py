# 균형잡힌 세상
import sys
input = sys.stdin.readline

while True:

    s = input().rstrip()

    if s == '.':
        break
    else:
        stack = []
        for i in s:
            if i in ['(', ')', '[', ']']:
                if not stack:
                    stack.append(i)
                else:
                    if stack[-1] == '(' and i == ')':
                        stack.pop()
                    elif stack[-1] == '[' and i == ']':
                        stack.pop()
                    else:
                        stack.append(i)
        print('yes' if not stack else 'no')
