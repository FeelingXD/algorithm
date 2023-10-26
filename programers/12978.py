# 배달
import heapq
from math import inf


def solution(N, roads, K):
    answer = 0
    graph = [[] for _ in range(N+1)]

    # 그래프 그리기
    # road = s,e,w
    for road in roads:
        s, e, w = road
        graph[s].append((e, w))
        graph[e].append((s, w))

    answer = daijkstra(1, graph, N)[1:]
    return sum([1 for i in answer if i <= K])


def daijkstra(s, graph, N):
    q = []
    distance = [inf for _ in range(N+1)]
    distance[s] = 0
    heapq.heappush(q, (0, s))

    while q:
        dist, now = heapq.heappop(q)

        if distance[now] < dist:
            continue

        for e, w in graph[now]:
            if dist+w < distance[e]:
                distance[e] = dist+w
                heapq.heappush(q, (dist+w, e))
    return distance
