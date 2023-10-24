# 프로세스
from collections import deque


def solution(priorities, location):
    marked_priorities = [[p, False] for p in priorities]
    marked_priorities[location][1] = True
    q = deque(marked_priorities)
    priorities.sort()
    answer = 1
    while q:
        p, m = q.popleft()
        if priorities and priorities[-1] == p:
            priorities.pop()
            if m:
                return answer
            answer += 1
        else:
            q.append([p, m])
