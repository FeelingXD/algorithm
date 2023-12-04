# 상자넣기
import sys
input =sys.stdin.readline

def solution():
    n=int(input())
    li=list(map(int,input().split()))
    dp=[1]*(n+1)
    for i in range(n):
        for j in range(i):
            if li[i]>li[j]:
                dp[i+1]=max(dp[i+1],dp[j+1]+1)
    print(max(dp))
    pass
if __name__=="__main__": # 실행되는 부분
    solution()
    pass