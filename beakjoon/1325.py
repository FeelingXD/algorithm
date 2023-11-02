# 효율적인 해킹
import sys
from collections import deque, defaultdict
input = sys.stdin.readline

N, M = map(int, input().split())
graph = [[] for _ in range(N+1)]


def bfs(s):
    q = deque([s])
    visited = [False]*(N+1)
    visited[s] = True
    cnt = 1
    while q:
        v = q.popleft()
        for i in graph[v]:
            if not visited[i]:
                visited[i] = True
                cnt += 1
                q.append(i)
    return cnt


if __name__ == "__main__":

    result = []

    # graph 그리기
    for _ in range(M):
        s, e = map(int, input().split())
        graph[e].append(s)
    # graph 순회
    answer = []
    for i in range(1, len(graph)):
        result.append(bfs(i))
    max_result = max(result)
    for i in range(len(result)):
        if result[i] == max_result:
            print(i+1, end=" ")
    pass
