# 회전초밥
import sys
input = sys.stdin.readline
n, d, k, c = map(int, input().split())
li = [int(input()) for _ in range(n)]

l, r = 0, 0
answer = 0

while l != n:
    r = l+k
    case = set()
    addable = True
    for i in range(l, r):
        case.add(li[i % n])
        if li[i % n] == c:
            addable = False
    cnt = len(case)
    if addable:
        cnt += 1
    answer = (max(answer, cnt))
    l += 1
print(answer)
