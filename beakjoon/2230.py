# 수고르기
import sys
input = sys.stdin.readline

case, gap = map(int, input().split())
nums = []
for i in range(case):
    nums.append(int(input()))
nums.sort()
strt = 0
end = 0
ans = int(2e10)
while strt <= end and end < case:
    if nums[end]-nums[strt] < gap:
        end += 1
    else:
        ans = min(ans, nums[end]-nums[strt])
        strt += 1
print(ans)
