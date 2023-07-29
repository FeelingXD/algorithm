# 주식
import sys
input = sys.stdin.readline
cases = int(input())

for t in range(cases):

    c_prices = int(input())
    prices = list(map(int, input().split()))

    value = 0
    max_value = 0

    for i in range(len(prices)-1, -1, -1):
        if (prices[i] > max_value):
            max_value = prices[i]
        else:
            value += max_value-prices[i]
    print(value)
