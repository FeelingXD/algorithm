# BaseBall
import sys
input = sys.stdin.readline

for _ in range(int(input())):
    score = [0, 0]
    for _ in range(9):
        v = list(map(int, input().split()))
        score = [score[0]+v[0], score[1]+v[1]]
    print("Yonsei" if score[0] > score[1]
          else "Korea" if score[1] > score[0] else "Draw")
