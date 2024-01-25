# 계단 오르기
import sys
input =sys.stdin.readline

def solution():
    n=int(input())
    stairs=[0]+[int(input()) for _ in range(n)]
    dp=[0]*(n+1)    
    if n<=2:
        return stairs[1] if n==1 else sum(stairs)
    
    dp[1]=stairs[1]
    dp[2]=stairs[1]+stairs[2]
    
    for i in range(3,n+1):
        dp[i] = max(dp[i-2]+stairs[i], dp[i-3]+stairs[i-1]+stairs[i])# 두칸뛰는 경우 와 3칸이전에서 띄우고 한칸 더하는경우
        
    return(dp[-1])
    pass
if __name__=="__main__": # 실행되는 부분
    print(solution())
    pass