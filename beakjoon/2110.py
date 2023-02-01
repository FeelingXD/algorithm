# 2110 공유기설치
import sys
input = sys.stdin.readline

case, routers = map(int, input().split())
house = []
for i in range(case):
    house.append(int(input()))

house.sort()
left = 1
right = house[-1]-house[0]
distance = 0
answer = 0

while left <= right:
    mid = (left+right)//2
    start = house[0]
    cnt = 1

    for i in range(1, len(house)):
        distance = house[i]-start

        if mid <= distance:
            cnt += 1
            start = house[i]

    if cnt >= routers:
        answer = mid
        left = mid+1
    else:
        right = mid-1
print(answer)
