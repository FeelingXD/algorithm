#돌 게임 3
import sys
input =sys.stdin.readline

def solution():
    n=int(input())
    dp=[1,1,0,1,1]
    for i in range(5,n+1):
        if (dp[i-4]+dp[i-3]+dp[i-1])==3:
            dp.append(0)
        else:
            dp.append(1)
    print("SK" if dp[n] else "CY")
    pass
if __name__=="__main__": # 실행되는 부분
    solution()
    pass