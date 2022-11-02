import sys
sys.setrecursionlimit(10**7)
fib_m = {0:0,1:1,2:1}
def solution(n):
    return fib(n)%1234567
def fib(n):
    if n in fib_m:
        return fib_m[n]
    fib_m[n]=fib(n-1)+fib(n-2)
    return fib_m[n]
print(solution(3333))

#bottom up dynamic programming
def solution2(n):
    dp=[0]*(n+1)
    dp[0]=0
    dp[1]=1
    for i in range(2,n+1):
        dp[i]=dp[i-1]+dp[i-2]
    return dp[n]
print(solution(5))