# 숫자고르기
import sys
from collections import defaultdict

input = sys.stdin.readline

dic = defaultdict(int)


def dfs(node, visited_set, target_set):
    if visited[node]:
        if visited_set == target_set:
            for v in visited_set:
                ans.add(v)
            return
        else:
            for v in visited_set:
                visited[v] = False
            return
    else:
        visited[node] = True
        next_node = dic[node]
        visited_set.add(node)
        target_set.add(next_node)
        dfs(next_node, visited_set, target_set)
    pass


def solution():
    global arr, visited, ans
    arr = [int(input()) for _ in range(int(input()))]
    ans = set()
    for i, v in enumerate(arr, 1):
        dic[i] = v
    visited = [False] * (len(arr) + 1)
    for i in dic.keys():
        if visited[i]:
            continue
        dfs(i, set(), set())
    ans = sorted(list(ans))

    print(len(ans))
    for v in ans:
        print(v)
    pass


if __name__ == "__main__":  # 실행되는 부분
    solution()
    pass
