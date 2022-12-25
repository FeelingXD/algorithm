# 떡볶이 떡 만들기

# 첫 째줄에 떡의 개수 N과 요청한 떡의 길이 M이 주어진다.
import sys
n, m = map(int, sys.stdin.readline().split())
cakes = list(map(int, sys.stdin.readline().split()))

# 이진탐색 시작점 끝점 생성
start = 0
end = max(cakes)

result = 0
while (start <= end):
    total = 0
    mid = (start + end)//2
    for cake in cakes:
        if cake > mid:
            total += cake-mid
    if total < m:
        end = mid-1
    else:
        result = mid
        start = mid + 1
print(result)
