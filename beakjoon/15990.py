#1,2,3 더하기 5
import sys
input =sys.stdin.readline
MOD=1_000_000_009
def solution():
    cases=[int(input()) for _ in range(int(input()))]
    maxNum=max(cases)
    dp=[[0]*4 for _ in range(maxNum+1)]
    dp[1][1]=1
    dp[2][2]=1
    dp[3][1]=1
    dp[3][3]=1
    dp[3][2]=1
    for i in range(4,maxNum+1):
        dp[i][1]=dp[i-1][3]%MOD+dp[i-1][2]%MOD
        dp[i][2]=dp[i-2][1]%MOD+dp[i-2][3]%MOD
        dp[i][3]=dp[i-3][1]%MOD+dp[i-3][2]%MOD
    print(dp)
    for v in cases:
        print(sum(dp[v])%MOD)
if __name__=="__main__": # 실행되는 부분
    solution()
    pass