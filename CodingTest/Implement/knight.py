# 8x8 체스판 나이트의 이동
# 초기값으로는 나이트의 위치를 받아오며 반환값은 움직일수있는 갯수
import sys
loc = list(sys.stdin.readline().strip())

col = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8}
steps = {(2, 1), (2, -1), (1, 2), (-1, 2), (-2, 1), (-2, 1), (1, -2), (-1, -2)}
current_area = [col[loc[0]], int(loc[1])]
answer = 0
for step in steps:
    next_row = int(loc[1])+step[0]
    next_col = col[loc[0]]+step[1]
    if next_row >= 1 and next_row <= 8 and next_col >= 1 and next_col <= 8:
        answer += 1
print(answer)
