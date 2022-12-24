# 성적이 낮은 순서로 출력하기

# 입력 : 첫줄에 학생수 입력
# 출력 : 낮은순서의 학생 이름이 나열할것

import sys

num = int(sys.stdin.readline().strip())
arr = []
for i in range(num):
    arr.append(list(sys.stdin.readline().split()))
arr.sort(key=lambda arr: int(arr[1]))

for i in arr:
    i[0]
    print(i[0], end=' ')
