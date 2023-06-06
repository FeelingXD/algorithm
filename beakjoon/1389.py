# 케빈 베이커 게임
import sys
from collections import deque, defaultdict
input = sys.stdin.readline

n, k = map(int, input().split())
graph = defaultdict(list)
scores = [0]
for _ in range(k):  # graph 작성
    s, d = map(int, input().split())
    graph[s].append(d)
    graph[d].append(s)


def bfs(s):
    q = deque()
    visited = [False]*(n+1)
    q.append([s, 1])
    cnt = 0
    while q:
        v, c = q.popleft()
        cnt += c
        for i in graph[v]:
            if not visited[i]:
                visited[i] = True
                q.append([i, c+1])
    return cnt-n


for i in range(1, n+1):
    scores.append(bfs(i))

print(scores.index(min(scores[1:])))
