# 부분수열의 합 bitmask
import sys
input = sys.stdin.readline

values = list(map(int, input().split()))
nums = list(map(int, input().split()))

cnt = 0
origin = bin(1 << values[0])

for i in range(1, 1 << values[0]):
    m = sum(nums[k] for k in range(values[0]) if (i & (1 << k) > 0))
    if m == values[1]:
        cnt += 1
print(cnt)
