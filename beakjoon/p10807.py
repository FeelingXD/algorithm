import sys
times = int(sys.stdin.readline())
nums = list(map(int, sys.stdin.readline().split()))
target = int(sys.stdin.readline())
print(nums.count(target))
