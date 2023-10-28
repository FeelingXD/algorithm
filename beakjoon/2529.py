# 부등호
import sys
from collections import deque
input = sys.stdin.readline
answer = []


def bfs(numbers, c_i, visited):
    if c_i == max_n:
        answer.append(numbers)
        return
    else:
        if c_i < 0:
            for i in range(10):
                visited[i] = True
                bfs([i], c_i+1, visited)
                visited[i] = False
        else:
            for i in range(10):
                if not visited[i]:
                    match brackets[c_i]:
                        case ">":
                            if numbers[-1] > i:
                                visited[i] = True
                                bfs(numbers+[i], c_i+1, visited)
                                visited[i] = False
                        case "<":
                            if numbers[-1] < i:
                                visited[i] = True
                                bfs(numbers+[i], c_i+1, visited)
                                visited[i] = False

    pass


if __name__ == "__main__":
    visited = [False for _ in range(10)]
    global max_n
    global brackets
    max_n = int(input())
    brackets = list(input().split())
    bfs([], -1, visited)
    print(''.join(map(str, answer[-1])))
    print(''.join(map(str, answer[0])))
