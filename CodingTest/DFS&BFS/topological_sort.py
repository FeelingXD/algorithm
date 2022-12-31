# 위상정렬
# example input
# 7 8
# 1 2
# 1 5
# 2 3
# 2 6
# 3 4
# 4 7
# 5 6
# 6 4

from collections import deque
import sys
input = sys.stdin.readline

v, e = map(int, input().split())
# 진입차수
indegree = [0 for i in range(v+1)]
graph = [[] for i in range(v+1)]

for _ in range(e):  # 간선
    a, b = map(int, input().split())
    graph[a].append(b)
    indegree[b] += 1

# 위상 정렬함수


def topology_sort():
    result = []
    q = deque()

    for i in range(1, v+1):
        if indegree[i] == 0:
            q.append(i)

    while q:
        now = q.popleft()
        result.append(now)
        for i in graph[now]:
            indegree[i] -= 1
            if indegree[i] == 0:
                q.append(i)
    for i in result:
        if i != result[-1]:
            print(i, end=' -> ')
        else:
            print(i)


topology_sort()
