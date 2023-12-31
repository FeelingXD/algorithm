# 동전 1
import sys
input =sys.stdin.readline

def solution():
    n,k=map(int,input().split())
    coins=[]
    for _ in range(n):
        coins.append(int(input()))
    coins.sort()
    dp=[0]*(k+1)
    dp[0]=1
    for coin in coins:
        for i in range(coin,k+1):
            dp[i]+=dp[i-coin]
    print(dp[-1])
    
    pass
if __name__=="__main__": # 실행되는 부분
    solution()
    pass