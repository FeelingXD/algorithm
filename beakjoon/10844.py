# 쉬운 계단수
import sys
input =sys.stdin.readline
MOD=1_000_000_000
def solution():
    n=int(input())
    dp=[[0]+[1]*9 for _ in range(n+1)]
    dp[0]=[0]*10
    for i in range(2,len(dp)):
        for j in range(10):
            match j:
                case 0:
                    dp[i][j]=dp[i-1][j+1]%MOD
                case 9:
                    dp[i][j]=dp[i-1][j-1]%MOD
                case x:
                    dp[i][j]=(dp[i-1][j-1]+dp[i-1][j+1])%MOD
    print(sum(dp[-1])%MOD)         
    pass
if __name__=="__main__": # 실행되는 부분
    solution()
    pass