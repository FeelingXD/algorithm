# 퇴사 2
import sys
input =sys.stdin.readline
def solution():
    n=int(input())
    dp=[0 for _ in range(n+1)]
    work_list=[]
    
    for _ in range(n):
        work_list.append(tuple(map(int,input().split())))
    
    for i in range(len(work_list)-1,-1,-1):
        t,v=work_list[i]
        
        if i+t > n:
            dp[i]=dp[i+1]
            continue
        else:
            dp[i]=max(dp[i+t]+v,dp[i+1])
    print(dp[0])
    pass
if __name__=="__main__": # 실행되는 부분
    solution()
    pass