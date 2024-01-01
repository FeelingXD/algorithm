# 동전 2
import sys
input =sys.stdin.readline

def solution():
    n,k=map(int,input().split())
    coins=set()
    for _ in range(n):
        coins.add(int(input()))
    coins=sorted(list(coins))
    dp=[10001]*(k+1)
    dp[0]=0
    for coin in coins:
        for i in range(coin,k+1):
            dp[i]=min(dp[i],dp[i-coin]+1)
    print(dp[-1] if dp[-1]!=10001 else -1)
    
    pass
if __name__=="__main__": # 실행되는 부분
    solution()
    pass