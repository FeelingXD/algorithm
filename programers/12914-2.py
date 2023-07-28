# 멀리 뛰기 (dp)
def solution(n):
    return fib(n) % 1234567


def fib(n):
    dp = [1 for i in range(n+1)]
    for i in range(2, n+1):
        dp[i] = dp[i-2]+dp[i-1]
    return dp[-1]
