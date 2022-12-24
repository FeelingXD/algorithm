# 위에서 아래로

# 첫째 줄 수열에 속해있는수의 개수 N이 주어진다.
# 출력 :내림차순으로 정렬

import sys

count = int(sys.stdin.readline().strip())
answer = []
for i in range(count):
    answer.append(int(sys.stdin.readline().strip()))
answer = sorted(answer, reverse=True)
print(answer)
