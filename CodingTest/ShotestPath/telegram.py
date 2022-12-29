# 전보

# 입력 첫줄에 도시개수 n 통로개수 m 메세지를 보내는 도시 c 가 주어진다

# 출력 첫줄에서 도시 C에서 보낸 메세지를 받는 도시의 총 개수와 걸리는 시간을 공백으로 출력

import sys
import heapq

input = sys.stdin.readline
INF = (1e9)  # 무한

n, m, start = map(int, input().split())

graph = [[] for i in range(n+1)]

distance = [INF]*(n+1)

for _ in range(m):
    x, y, z = map(int, input().split())
    graph[x].append((y, z))


def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))


dijkstra(start)

count = 0
max_distance = 0
for d in distance:
    if d is not INF:
        count += 1
        max_distance = max(max_distance, d)

print(count-1, max_distance)
