# 등굣길
def solution(m, n, puddles):
    maps = [[0]*(m+1) for i in range(n+1)]
    maps[1][1] = 1
    for i in range(1, n+1):
        for j in range(1, m+1):
            if i == 1 and j == 1:
                continue
            if [j, i] in puddles:
                maps[i][j] = 0
            else:
                maps[i][j] = maps[i-1][j]+maps[i][j-1]
    for i in maps:
        print(i)
    return maps[i][j] % 1000000007


solution(1, 1, [[1, 1]])
