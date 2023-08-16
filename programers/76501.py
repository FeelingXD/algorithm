# 음양 더하기
from functools import reduce


def solution(absolutes, signs):
    answer = reduce(lambda x, y: (x[0]+y[0], True) if y[1] else (x[0]-y[0], True),
                    list(zip(absolutes, signs)), (0, True))
    return answer[0]
