# 반복수열
import sys
input = sys.stdin.readline

num, num2 = map(int, input().split())

dp = [0]*25000
dp[1] = num
cast = []
index = 1
while True:
    tot = 0
    tmp = dp[index]
    index += 1
    while tmp > 0:
        tot += pow(tmp % 10, num2)
        tmp //= 10

    if tot in dp:
        print(max(dp.index(tot)-1, 0))
        break
    else:
        dp[index] = tot
