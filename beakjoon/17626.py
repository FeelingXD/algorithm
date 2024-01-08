# Four Squares
import sys
input =sys.stdin.readline

def solution():
    n=int(input())
    dp=[i for i in range(n+1)]
    for i in range(1,n+1):
        for j in range(1,int(i**(1/2))+1):
            dp[i]=min(dp[i],dp[i-j**2]+1)
    print(dp[n])
    
    pass
if __name__=="__main__": # 실행되는 부분
    solution()
    pass