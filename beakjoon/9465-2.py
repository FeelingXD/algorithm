# 스티커
import sys
input =sys.stdin.readline

def solution():
    for _ in range(cases:=int(input())):
        n= int(input())
        dp=[[0]*(n+1) for _ in range(2)]
        
        board=[]
        board.append(list(map(int,input().split())))
        board.append(list(map(int,input().split())))
        
        dp[0][1]=board[0][0]
        dp[1][1]=board[1][0]
        
        for x in range(2,n+1):
            for y in range(2):
                if y:
                    dp[y][x]=max([dp[y][x-1],board[y][x-1]+dp[y][x-2],dp[y-1][x-1]+board[y][x-1]])
                    pass
                else:
                    dp[y][x]=max([dp[y][x-1],board[y][x-1]+dp[y][x-2],dp[y+1][x-1]+board[y][x-1]])
                    pass
        print(max(dp[0][-1],dp[1][-1]))
    pass
if __name__=="__main__": # 실행되는 부분
    solution()
    pass