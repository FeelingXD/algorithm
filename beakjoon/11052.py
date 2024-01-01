# 카드 구매하기
import sys
input =sys.stdin.readline

def solution():
    n=int(input())
    values=list(map(int,input().split()))
    dp=[0]*(n+1)
    # i 가 카드팩 들어있는갯수
    for s,v in enumerate(values,1):
        for i in range(s,n+1):
            dp[i]=max(dp[i-s]+v,dp[i])
    print(dp[-1])
        
    pass
if __name__=="__main__": # 실행되는 부분
    solution()
    pass