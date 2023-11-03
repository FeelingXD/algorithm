#퇴사
import sys
input = sys.stdin.readline

if __name__ == "__main__":
    
    work_list=[]
    for _ in range(n:=int(input())):
        work_list.append(tuple(map(int,input().split())))
    dp=[0]*(n+1)
    for i in range(n-1,-1,-1):
        d,v=work_list[i] # d 수행일수, v 가치
        if d+i<=n: # dp 의 인덱스를 넘으면안됨 
            dp[i]=max(dp[i+d]+v,dp[i+1]) # i의최대값은 n-1 부터시작 이전까지의 최대값이거나
            continue
        else:
            dp[i]=dp[i+1]
    print(dp[0])
    pass