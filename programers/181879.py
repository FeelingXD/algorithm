# 길이에 따른 연산
from functools import reduce


def solution(num_list):
    return reduce(lambda x, y: x*y, num_list, 1) if len(num_list) <= 10 else sum(num_list)
