import sys
sys.setrecursionlimit(10**7)
fib_m = {1:1,2:2}
def solution(n):
    return fib(n)%1234567
def fib(n):
    if n in fib_m:
        return fib_m[n]
    fib_m[n]=fib(n-1)+fib(n-2)
    return fib_m[n]%1234567

#dp bottom up

def solution(n):
    dp=[0]*(n+1)
    dp[1]=1
    dp[2]=2
    for i in range(3,n+1):
        dp[i]=dp[i-1]+dp[i-2]
    return dp[n]%12334567