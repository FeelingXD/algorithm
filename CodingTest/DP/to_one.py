# 1로만들기

# x가 5로나누어 떨어질경우 5로나눈다.
# x가 3으로 나누어 떨어질경우 3으로나눈다
# x가 2로나누어떨어질경우 2로나눈다
# x 에서 1을뺀다

import sys

m = int(sys.stdin.readline().strip())
dp = [0]*(m+1)
for i in range(2, m+1):
    dp[i] = dp[i-1]+1
    if i % 2 == 0:
        dp[i] = min(dp[i], dp[i//2]+1)
    if i % 3 == 0:
        dp[i] = min(dp[i], dp[i//3]+1)
    if i % 5 == 0:
        dp[i] = min(dp[i], dp[i//5]+1)
print(dp[m])
