# 2xn 타일링
import sys
input =sys.stdin.readline
MOD=1_000_7
def solution():
    n=int(input())
    dp=[0]*(1000+1)
    dp[1]=1
    dp[2]=2
    for i in range(3,n+1):
        dp[i]=(dp[i-1]%MOD+dp[i-2]%MOD)%MOD
    print(dp[n]%MOD if dp[n] else dp[n])
    pass
if __name__=="__main__": # 실행되는 부분
    solution()
    pass