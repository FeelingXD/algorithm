# 동전
import sys
input =sys.stdin.readline
def coin():
    types=int(input())
    coins=list(map(int,input().split()))
    target=int(input())
    dp=[0]*(target+1)
    # init 
    dp[0]=1
    for coin in coins:
        for i in range(coins[0],len(dp)):
            if i>=coin:
                dp[i]+=dp[i-coin]
    print(dp[-1])
    
    
def solution():
    for _ in range(case:=int(input())):
        coin()
    pass
if __name__=="__main__": # 실행되는 부분
    solution()
    pass