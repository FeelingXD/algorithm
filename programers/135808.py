# 과일 장수
from functools import reduce


def solution(k, m, score):
    answer = 0
    score.sort()
    score = score[len(score) % m:]
    return reduce(lambda acc, i: acc+score[i*m]*m, range(len(score)//m), 0)
