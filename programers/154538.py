# 숫자 변환하기
from collections import deque


def solution(x, y, n):
    if x >= y:
        return 0
    answer = 0

    q = deque([x])
    check = [0]*1000001

    while 1:
        answer += 1
        for _ in range(len(q)):
            c = q.popleft()

            if c*2 == y or c*3 == y or c+n == y:
                return answer

            if c*3 < y and not check[c*3]:
                q.append(c*3)
                check[c*3] += 1

            if c*2 < y and not check[c*2]:
                q.append(c*2)
                check[c*2] += 1

            if c+n < y and not check[c+n]:
                q.append(c+n)
                check[c+n] += 1
        if not len(q):
            return -1
