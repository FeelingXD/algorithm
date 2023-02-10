def solution(image: list, K: int):
    '''
        img: img
        K: 홀수 , 변의길이
    '''
    N = len(image[0])
    M = len(image)
    dp = [[0]*(N+1) for i in range(M+1)]
    result = [[0]*(N) for i in range(M)]
    for i in range(N+1):
        for j in range(M+1):
            dp[i][j] = dp[i-1][j] + dp[i][j-1] - dp[i-1][j-1]+image[i-1][j-1]
    print(dp)
    for i in range(1, N+1):
        for j in range(1, M+1):

            x1 = max(1, i - (K-1)//2)
            y1 = max(1, j - (K-1)//2)
            x2 = min(N, i + (K-1)//2)
            y2 = min(M, j + (K-1)//2)

            rangeSum = dp[x2][y2] - dp[x1-1][y2] - \
                dp[x2][y1-1] + dp[x1-1][y1-1]
            result[i-1][j-1] = rangeSum//(K*K)
    for i in result:
        print(i)


'''
    {{4, 5, 2, 6, 7},
            {5, 4, 2, 4, 6},
            {6, 8, 4, 8, 7},
            {7, 3, 6, 6, 4},
            {5, 0, 4, 1, 5}}
    
'''
'''
{{2, 2, 2, 3, 2},
 {3, 4, 4, 5, 4},
 {3, 5, 5, 5, 3},
 {3, 4, 4, 5, 3},
 {1, 2, 2, 2, 1}}
'''

print("🐍 File: review/marginalMean.py | Line: 16 | undefined ~ solution", solution(
    [[4, 5, 2, 6, 7],
     [5, 4, 2, 4, 6],
     [6, 8, 4, 8, 7],
     [7, 3, 6, 6, 4],
     [5, 0, 4, 1, 5]], 3))
