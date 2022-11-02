# 킹, 퀸, 룩, 비숍, 나이트, 폰
#  1 1 2 2 2 8
solution = []
chess_set = [1,1,2,2,2,8]
value = list(map(int, input().split()))

for i in range(len(chess_set)):
    solution.append(chess_set[i]-value[i])

print(*solution)
