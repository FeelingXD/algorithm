import sys
input = sys.stdin.readline
cnt = 0
for _ in range(int(input())):
    stack = []
    for c in input().strip():
        if not stack:
            stack.append(c)
        else:
            if stack[-1] == c:
                stack.pop()
            else:
                stack.append(c)
    if not stack:
        cnt += 1
print(cnt)
