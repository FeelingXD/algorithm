# 1,2,3 더하기 7
import sys
input =sys.stdin.readline
MOD=1_000_000_009
def solution():
    li=[]
    max_num=0
    for _ in range(int(input())):
        li.append(t:=tuple(map(int,input().split())))
        max_num=max(t[0],max_num)
    dp=[[0]*1001 for _ in range(1001)]
    dp[1][1]=1
    dp[2][1]=1
    dp[3][1]=1
    dp[0][0]=1
    for i in range(2,max_num+1):
        for j in range(2,max_num+1):
            if i-1>0:
                dp[i][j]+=dp[i-1][j-1]%MOD
            if i-2>0:
                dp[i][j]+=dp[i-2][j-1]%MOD
            if i-3>0:
                dp[i][j]+=dp[i-3][j-1]%MOD
    for target,num in  li:
        print(dp[target][num]%MOD)
    pass
if __name__=="__main__": # 실행되는 부분
    solution()
    pass