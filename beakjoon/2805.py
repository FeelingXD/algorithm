# 나무자르기
import sys
input = sys.stdin.readline

# case[0]== tree num, case[1] 가져가려는 나무높이
cases = list(map(int, input().split()))
trees = list(map(int, input().split()))
trees.sort()

left = 0
right = trees[-1]
mid = 0

while left <= right:
    mid = (left+right)//2
    if sum([i-mid for i in trees if i >= mid]) >= cases[1]:
        left = mid+1
    else:
        right = mid-1
print(right)
