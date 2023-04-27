# 촌수계산

node = int(input())
a, b = map(int, input().split())
edges = int(input())
graph = [[] for i in range(node+1)]
visited = [False]*(node+1)
result = []
for _ in range(edges):

    s, e = map(int, input().split())
    graph[s] += [e]
    graph[e] += [s]


def dfs(v, cnt):
    visited[v] = True

    if v == b:
        result.append(cnt)

    for i in graph[v]:
        if not visited[i]:
            dfs(i, cnt+1)


dfs(a, 0)

print(result[0] if len(result) != 0 else -1)
