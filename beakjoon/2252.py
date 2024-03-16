# 줄세우기
import sys
from collections import deque, defaultdict

input = sys.stdin.readline


def solution():
    n, m = map(int, input().split())
    inDegree = defaultdict(int)
    graph = defaultdict(list)
    q = deque()
    ans = []
    for _ in range(m):
        s, e = map(int, input().split())
        graph[s].append(e)
        inDegree[e] += 1

    for i in range(1, n + 1):
        if inDegree[i] == 0:
            q.append(i)

    while q:
        tmp = q.popleft()
        ans.append(tmp)
        for i in graph[tmp]:
            inDegree[i] -= 1
            if not inDegree[i]:
                q.append(i)
    print(*ans)
    pass


if __name__ == "__main__":  # 실행되는 부분
    solution()
    pass
