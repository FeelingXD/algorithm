# 5-8

def dfs(graph, v, visited):
    visited[v] = True
    print(v, end=' ')
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)


test = [
    [],
    [2, 3, 8],
    [1, 7],
    [1, 4, 5],
    [3, 5],
    [3, 4],
    [7],
    [2, 6, 8],
    [1, 7]
]
visited = [False for i in range(len(test))]
print("🐍 File: DFS&BFS/example_DFS.py | Line: 23 | undefined ~ visited", visited)

dfs(test, 1, visited)
