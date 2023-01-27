# 주식 가격
from collections import deque


def solution(prices):
    answer = []
    prices = deque(prices)
    while prices:
        cnt = 0
        c = prices.popleft()
        for i in prices:
            cnt += 1
            if i < c:
                break
        answer.append(cnt)
    return answer
