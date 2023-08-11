# 도키도키 간식드리미
import sys
input = sys.stdin.readline

case = int(input())
order = list(map(int, input().split()))
stack = []
current = 1

able = True
for v in order:
    if v == current:
        current += 1
    else:
        while stack and stack[-1] == current:
            current += 1
            stack.pop()
        if not stack or stack[-1] > v:
            stack.append(v)
        else:
            able = False
            break

print("Nice") if able else print("Sad")
