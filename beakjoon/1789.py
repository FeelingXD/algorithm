# 수들의 합
import sys
from collections import deque
input = sys.stdin.readline
'''
서로 다른 N개의 자연수의 합이 S라고 한다. S를 알 때, 자연수 N의 최댓값은 얼마일까?

'''


if __name__ == "__main__":  # 문제를 푸는 영역
    N = int(input())
    near_target = 0
    cnt = 0
    while near_target < N:
        near_target += cnt
        cnt += 1
    print(cnt-2 if N < near_target else cnt-1)
    pass
