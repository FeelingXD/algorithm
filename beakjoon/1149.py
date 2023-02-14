# rgb 거리
import sys
input = sys.stdin.readline
dp = [[0]*3 for _ in range(1001)]
dp[0][0], dp[0][1], dp[0][2] = 0, 0, 0
li = []
case = int(input())


for i in range(case):
    li.append(list(map(int, input().split())))

for i in range(1, case+1):
    dp[i][0] = min(dp[i-1][1], dp[i-1][2])+li[i-1][0]
    dp[i][1] = min(dp[i-1][0], dp[i-1][2])+li[i-1][1]
    dp[i][2] = min(dp[i-1][0], dp[i-1][1])+li[i-1][2]

print(min(dp[case]))
