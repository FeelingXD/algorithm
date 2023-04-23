
# 바이러스(dfs)
n = int(input())
v = int(input())
graph = [[] for i in range(n+1)]
visited = [False]*(n+1)


for i in range(v):
    a, b = map(int, input().split())
    graph[a] += [b]
    graph[b] += [a]


def dfs(start_node):
    visited[start_node] = True
    for i in graph[start_node]:
        if not visited[i]:
            dfs(i)


dfs(1)
print(visited.count(True)-1)
