# 텀프로젝트
import sys
from collections import deque

input = sys.stdin.readline


def init_visited(size):
    return [False] * size


def visited_index(visited):
    if not visited:
        return []
    return [i for i, v in enumerate(visited) if v]


def bfs(s, graph):
    """
    s : 시작노드
    graph : graph
    """
    visited = init_visited(len(graph) + 1)
    q = deque()
    q.append(s)
    visited[s] = True
    member_cnt = 1
    while q:
        next_node = graph[q.popleft()]
        if not visited[next_node]:
            q.append(next_node)
            visited[next_node] = True
            member_cnt += 1
        else:
            if next_node == s:
                # 다음노드가 시작노드로 사이클이되었을경우
                return (visited, member_cnt)
    return ([], 0)

    pass


def solution():

    for _ in range(case := int(input())):
        n = int(input())
        students = list(map(int, input().split()))
        students = {i: v for i, v in enumerate(students, 1)}
        check_list = set()
        team_member = 0
        for i in range(1, n + 1):
            if i not in check_list:
                cycle, cnt = bfs(i, graph=students)
                if cycle:
                    check_list.update(visited_index(cycle))
                    team_member += cnt
            pass
        pass
        print(n - team_member)
    pass


if __name__ == "__main__":  # 실행되는 부분
    solution()
    pass
