# 큰 수의 법칙
# 설명 : 주어진 수 들을 M번 더하여 가장 큰수를 만드는 법칙 하지만 연속적으로
# K번을 초과하여 더할수없음

# 입력조건 첫줄에 자연수 N M K 가 주어지며 각 자연수는 공백으로 구분한다.
# 둘째 줄에서 N개의 자연수가 주어진다. 자연수는 공백으로 구분한다.
# 단, 각각의 자연수는 1이상 1만 이하의 수로주어진다.
# K<=M 을 항상 만족한다.

# K=max sequence , M = amount ,N =len(list(input)

import sys
K, M, N = map(int, sys.stdin.readline().split(' '))
data = list(map(int, sys.stdin.readline().split()))
data.sort(reverse=True)

fst_data = data[0]
sec_data = data[1]

answer = 0
for i in range(M):
    if i != 0 and K % i == 0:
        answer += sec_data
    else:
        answer += fst_data
print(answer)
