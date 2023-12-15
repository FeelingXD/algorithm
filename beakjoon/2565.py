# 전깃줄
import sys
input =sys.stdin.readline

def solution():
    lines=[]
    for _ in range(n:=int(input())):
        lines.append(tuple(map(int,input().split())))
    lines.sort()
    dp=[1]*(n+1)
    for i in range(1,n):
        for j in range(i):
            if lines[j][1] < lines[i][1]:
                dp[i]=max(dp[i],dp[j]+1)
    print(n-max(dp))
    pass
if __name__=="__main__": # 실행되는 부분
    solution()
    pass
