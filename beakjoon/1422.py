# 숫자의신
import sys
input = sys.stdin.readline


n, k = map(int, input().split())
nums = []
max_n = 0
for _ in range(n):
    v = input().rstrip()
    nums.append(v)
    max_n = max(max_n, int(v))

for _ in range(k-n):
    nums.append(str(max_n))

nums.sort(key=lambda x: x*100, reverse=True)

print("".join(nums))
