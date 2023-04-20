# 괄호

case = int(input())
parenthesis = []
for _ in range(case):
    parenthesis.append(input())

for i in parenthesis:
    stack = []
    for j in i:
        if not stack:
            stack.append(j)
        else:
            if stack[-1] == '(' and j == ')':
                stack.pop()
            else:
                stack.append(j)
    print('YES') if not stack else print('NO')
