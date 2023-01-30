# 부녀 회장이 될테야
import sys
input = sys.stdin.readline
''' 
    3 : 1  5  15 35 70 126
    2 : 1  4  10 20 35 56
    1 : 1  3  6  10 15 21.. . (n-1)
    0 : 1 ,2 ,3 ,4  5  6. .. i
'''
# dp[n][m-1]
case_stair = []
case_room = []
case = int(input())
for _ in '*'*case:
    case_stair.append(int(input()))
    case_room.append(int(input()))

dp = [[i for i in range(1, max(case_room)+1)]
      for j in range(max(case_stair)+1)]
for i in range(1, max(case_stair)+1):
    for j in range(max(case_room)):
        dp[i][j] = sum(dp[i-1][:j+1])

for i in zip(case_stair, case_room):
    stair, room = i
    print(dp[stair][room-1])
