# 1,2,3 더하기6
import sys
input =sys.stdin.readline
MOD=1_000_000_009

    
def solution():
    global dp
    li=[int(input()) for _ in range(int(input()))]
    max_num=max(li)
    dp=[0]*(max_num+1)
    dp[0]=1
    dp[1]=1
    dp[2]=2
    dp[3]=2
    for i in range(4,max_num+1):
        if i-6>=0:
            dp[i]+=dp[i-6]%MOD
        dp[i]+=dp[i-4]%MOD+dp[i-2]%MOD
    for v in li:
        print(dp[v]%MOD)
    pass
if __name__=="__main__": # 실행되는 부분
    solution()
    pass