# 기사단원의 무기
from functools import reduce


def get_len_measures(n):
    if n == 1:
        return 1
    else:
        cnt = 0
        for i in range(1, int(n**(1/2))+1):
            if n % i == 0:
                if i**2 == n:
                    cnt += 1
                else:
                    cnt += 2
        return cnt


def solution(number, limit, power):
    answer = reduce(lambda x, y: x+get_len_measures(y) if get_len_measures(y)
                    <= limit else x+power, range(2, number+1), 1)
    return answer
