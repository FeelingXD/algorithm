# UCPC는 무엇의 약자일까?
import sys
input = sys.stdin.readline

words = list(input().split())
check = ['U', 'C', 'P']
stack = []
for word in words:
    for c in word:
        if c in word:
            stack.append(c)
cnt = 0
target = 'UCPC'
for c in stack:
    if cnt < len(target) and c == target[cnt]:
        cnt += 1
print('I love UCPC' if cnt == 4 else 'I hate UCPC')
