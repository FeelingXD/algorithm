# 1,2,3 더하기 8
import sys
input =sys.stdin.readline
MOD=1_000_000_009
def solution():
    li=[]
    max_num=0
    for _ in range(int(input())):
        li.append(t:=int(input()))
        max_num=max(t,max_num)
    dp=[[0,0] for _ in range(max_num+1)]
    dp[0][0]=1
    dp[1][0]=1
    dp[2][0]=1
    dp[2][1]=1
    dp[3][0]=2  #111,3
    dp[3][1]=2
    for i in range(4,max_num+1):
        dp[i][1]=(dp[i-3][0]%MOD+dp[i-2][0]%MOD+dp[i-1][0]%MOD)%MOD
        dp[i][0]=(dp[i-3][1]%MOD+dp[i-2][1]%MOD+dp[i-1][1]%MOD)%MOD
        
    for target in  li:
        print(*dp[target])
    pass
if __name__=="__main__": # 실행되는 부분
    solution()
    pass