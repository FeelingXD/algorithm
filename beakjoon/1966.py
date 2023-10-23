# 프린터큐
import sys
from collections import deque
input = sys.stdin.readline


def solution():

    n, t = map(int, input().split())  # 문서 갯수 와 목표 문서
    documents = list(map(int, input().split()))
    importance_list = documents.copy()
    importance_list.sort()
    printer_q = deque([[importance, False] for importance in documents])
    printer_q[t][1] = True
    cnt = 1
    while printer_q:
        i, t = printer_q.popleft()

        if importance_list[-1] == i:
            if t:
                return cnt
            importance_list.pop()
            cnt += 1
        else:
            printer_q.append([i, t])


if __name__ == "__main__":
    for _ in range(case := int(input())):
        print(solution())
    pass
