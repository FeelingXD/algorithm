# 트리의 부모찾기 bfs
from collections import deque
node = int(input())

graph = [[] for i in range(node+1)]
visited = [False]*(node+1)
dic = {}
q = deque()

for _ in range(node-1):
    s, e = map(int, input().split())
    graph[s] += [e]
    graph[e] += [s]

q.append((1, graph[1]))


def bfs(start):
    while q:
        current, nodes = q.popleft()
        for i in nodes:
            if dic.get(i, 0) == 0:
                dic[i] = current
                q.append((i, graph[i]))


bfs(1)
for i in range(2, node+1):
    print(dic[i])
