# 요세푸스 문제
import sys
import collections
input = sys.stdin.readline

n, k = map(int, input().split())

q = collections.deque([i for i in range(1, n+1)])
cnt = 1
print("<", end="")
while 1 < len(q):
    if cnt == k:
        print(q.popleft(), end=", ")
        cnt = 1
    else:
        q.append(q.popleft())
        cnt += 1
print(q.popleft(), end=">")
