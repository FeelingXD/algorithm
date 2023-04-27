# 온라인판매
import sys
input = sys.stdin.readline

eggs, customer = map(int, input().split())

prices = []
for _ in range(customer):
    prices.append(int(input()))

prices.sort(reverse=True)

v = min(eggs, customer)
mx = 0
mp = 0
for i in range(v):
    if prices[i]*(i+1) > mx:
        mp = prices[i]
        mx = prices[i]*(i+1)
print(mp, mx)
