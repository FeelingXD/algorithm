# 숨바꼭질
import sys
from collections import deque, defaultdict

N, E = map(int, input().split())
visited = [False for i in range(N+1)]

dic = defaultdict(set)
for _ in range(E):
    s, e = map(int, input().split())
    dic[s].add(e)
    dic[e].add(s)
q = deque([[1, 0]])
visited[1] = True
max_depth = 0
answer = [[], max_depth]
while q:
    s, depth = q.popleft()
    if depth > max_depth:
        max_depth = depth
        answer = [[], max_depth]
    if depth == max_depth:
        answer[0].append(s)
    for next in dic[s]:
        if not visited[next]:
            visited[next] = True
            q.append([next, depth+1])
print(f'{min(answer[0])} {answer[1]} {len(answer[0])}')
