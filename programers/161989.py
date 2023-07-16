# 덧칠하기
from collections import deque


def solution(n, m, section):
    section = deque(section)
    cnt = 0
    while section:
        v = section.popleft()
        roller_range = v+m
        cnt += 1
        while section and section[0] < roller_range:
            v = section.popleft()
    return cnt
