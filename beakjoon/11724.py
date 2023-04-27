# 연결 요소의 개수
import sys
sys.setrecursionlimit(10**5)
input = sys.stdin.readline

node, edge = map(int, input().split())
# graph = [[] for i in range(node+1)]
graph = {}
visited = [False]*(node+1)
cnt = 0


def dfs(s):
    visited[s] = True
    for i in graph.get(s, []):
        if not visited[i]:
            dfs(i)


for _ in range(edge):
    s, e = map(int, input().split())
    graph[s] = graph.get(s, [])+[e]
    graph[e] = graph.get(e, [])+[s]


# for _ in range(edge):
#     s, e = map(int, input().split())
#     graph[s].append(e)
#     graph[e].append(s)

for i in range(1, node+1):
    if not visited[i]:
        dfs(i)
        cnt += 1

print(cnt)
