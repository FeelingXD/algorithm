# 삼총사
from itertools import combinations


def solution(number):
    return len([i for i in combinations(number, 3) if sum(i) == 0])
