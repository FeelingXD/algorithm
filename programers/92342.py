# 양궁 대회
from collections import deque


def solution(n, info):
    answer = [0]*10
    apeach_score = sum([10-i for i in range(10) if info[i]])
    able_score = [(10-i)*2 if info[i] else 10-i for i in range(10)]
    if n == info[0]:
        return [-1]
    q = deque([[0], [info[0]+1]])
    able = False
    while q:
        r = q.popleft()
        if sum(r) == n or len(r) == 10:
            new_r_score = sum([able_score[i] for i in range(len(r)) if r[i]])
            old_score = sum([able_score[i]
                            for i in range(len(answer)) if answer[i]])
            if apeach_score < new_r_score and new_r_score >= old_score:
                able = True
                answer = r
        elif sum(r)+info[len(r)]+1 <= n:
            q.append(r+[info[len(r)]+1])
            q.append(r+[0])
        else:
            q.append(r+[0])

    return answer+[0]*(10-len(answer))+[n-sum(answer)] if able else [-1]
