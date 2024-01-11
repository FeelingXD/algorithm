# 자두나무
import sys
input =sys.stdin.readline

def solution():
    T,W=map(int,input().split())
    plums=[0]+[int(input()) for _ in range(T)]
    dp=[[0,0] for _ in range(T+1)]
    
    
    for i in range(1,len(plums)):
        dp[i][0]=dp[i-1][0]+1 if plums[i]%2 else dp[i-1][0]
        
    for w in range(1, W+1): # 자리 바꾸는 기회
        for t in range(w,T+1): #자리바꾸기
            if w%2 : #홀수번째 이동 일때는
                if not plums[t]%2: # 2번 떨어지는 경우
                    dp[t][1]=max(dp[t-1])+1
                else:
                    dp[t][1]=dp[t-1][1]
            else: #짝수번째 이동
                if plums[t]%2: # 1번나무에서 떨어지는경우
                    dp[t][0]=max(dp[t-1])+1
                else:
                    dp[t][0]=dp[t-1][0]
    print(max(dp[-1]))
    
    pass
if __name__=="__main__": # 실행되는 부분
    solution()
    pass