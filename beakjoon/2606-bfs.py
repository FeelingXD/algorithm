from collections import deque
# 바이러스(bfs)
n = int(input())
v = int(input())
graph = [[] for i in range(n+1)]
visited = [False]*(n+1)

for i in range(v):
    a, b = map(int, input().split())
    graph[a] += [b]
    graph[b] += [a]

q = deque(graph[1])


def bfs(q: deque, graph, visited: list):
    visited[1] = True
    while q:
        c = q.popleft()
        if not visited[c]:
            visited[c] = True
            q.extend(graph[c])


bfs(q, graph, visited)
print(visited.count(True)-1)
