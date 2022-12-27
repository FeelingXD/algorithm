# 4 7
# 1 2 4
# 1 4 6
# 2 1 3
# 2 3 7
# 3 1 5
# 3 4 4
# 4 3 2


# 플로이드ㅡ 워셜 알고리즘
import sys
INF = int(1e9)
input = sys.stdin.readline

# 노드및 간선갯수
n, m = map(int, input().split())

#
graph = [[INF]*(n+1) for _ in range(n+1)]
# 비용 초기화 자기자신
for a in range(1, n+1):
    for b in range(1, n+1):
        if a == b:
            graph[a][b] = 0
# 간선정보 입력받기
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a][b] = c
# 플로이드 워셜 알고리즘 수행
for k in range(1, n+1):
    for a in range(1, n+1):
        for b in range(1, n+1):
            graph[a][b] = min(graph[a][b], graph[a][k]+graph[k][b])
# 출력문

for a in range(1, n+1):
    for b in range(1, n+1):
        # 도달 불가능 => inf
        if graph[a][b] == INF:
            print(f'{a} to {b} is imposible', end='/ ')
        else:
            print(f'{a} to {b} : {graph[a][b]}', end='/ ')
    print()
