# 가장 큰 정사각형 찾기
def solution(board):
    answer = 0
    for line in board:
        if 1 in line:
            answer=1
            break
            
    dp=[[0]*(len(board[0])+1)for _ in range(len(board)+1)]
    for y in range(1,len(dp)):
        for x in range(1,len(dp[0])):
            dp[y][x]=board[y-1][x-1]
            if board[y-1][x-1] and dp[y-1][x] and dp[y][x-1] and dp[y-1][x-1]:
                dp[y][x]=min(dp[y-1][x],dp[y][x-1],dp[y-1][x-1])+1
                answer=max(answer,dp[y][x])

    return answer**2