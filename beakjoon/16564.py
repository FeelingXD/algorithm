# 히오스 프로게이머
import sys
input = sys.stdin.readline

levels = []
C_cnt, k = map(int, input().split())  # 캐릭터 갯수, 올릴수있는레벨

for _ in '*'*C_cnt:
    levels.append(int(input()))
levels.sort()

left = levels[0]
right = levels[-1]+k
tmp = k

while left <= right:
    k = tmp
    mid = (left+right)//2
    for i in levels:
        if i < mid:
            k -= mid-i
    if k < 0:
        right = mid-1
    else:
        left = mid+1
print(right)
