# 예산
case = int(input())
lands = list(map(int, input().split()))
lands.sort()
max_t = int(input())

left = 0
right = lands[-1]
ret = 0
while left <= right:
    mid = (left+right)//2

    tmp = sum([min(i, mid) for i in lands])
    if tmp <= max_t:
        left = mid+1
    else:
        right = mid-1
print(right)
