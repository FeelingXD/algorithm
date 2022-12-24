# 두 배열의 원소 교체

# 입력
# 첫줄에 배열크기 n , 최대 바꿀수있는 갯수 k 가주어진다.
import sys

n, k = map(int, sys.stdin.readline().split())
a = list(map(int, sys.stdin.readline().split()))
b = list(map(int, sys.stdin.readline().split()))

change = 0
a.sort()
b.sort(reverse=True)
for i in range(k):
    if a[i] < b[i]:
        a[i], b[i] = b[i], a[i]
    else:
        break
print(sum(a))
