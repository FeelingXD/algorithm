# 귤 골르기
from collections import Counter


def solution(k, tangerine):
    answer = 0
    tangerine = Counter(tangerine)
    for i, value in enumerate(tangerine.most_common()):
        answer += value[1]
        if k <= answer:
            return i+1
