# 미래도시

# example input1
# 5 7
# 1 2
# 1 3
# 1 4
# 2 4
# 3 4
# 3 5
# 4 5
# 4 5
# exaple input2
# 4 2
# 1 3
# 2 4
# 3 4
import sys

input = sys.stdin.readline
INF = int(1e9)
# 노드 간선
n, m = map(int, input().split())

graph = [[INF]*(n+1) for _ in range(n+1)]

for a in range(1, n+1):
    for b in range(1, n+1):
        if a == b:
            graph[a][b] == 0

for _ in range(m):
    a, b = map(int, input().split())
    graph[a][b] = 1
    graph[b][a] = 1

x, k = map(int, input().split())  # 경유지, 최종목적지

for k in range(1, n+1):
    for a in range(1, n+1):
        for b in range(1, n+1):
            graph[a][b] = min(graph[a][b], graph[a][k]+graph[k][b])
distance = graph[1][k] + graph[k][x]

# print
if distance >= INF:
    print('-1')
else:
    print(distance)
