# 포도주 시식
import sys
input =sys.stdin.readline

def solution():
    
    # 포도주
    wines=[0]
    
    for i in range(n:=int(input())):
        wines.append(int(input()))
    dp=wines.copy()
    
    if n==1:
        return(dp[1])
    elif n==2:
        return(dp[1]+dp[2])
    
    dp[2]=dp[1]+dp[2]
    for i in range(3,len(dp)):
        dp[i]=max(dp[i-2]+wines[i],dp[i-3]+wines[i-1]+wines[i],dp[i-1])
    return(dp[-1])        
    
    pass
if __name__=="__main__": # 실행되는 부분
    print(solution())
    pass