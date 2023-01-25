# 스택 수열
import sys
input = sys.stdin.readline

cnt = int(input())
nums = []  # input
stack = []  # stack
result = []  # result
for _ in range(cnt):
    nums.append(int(input()))

idx = 0
for i in range(len(nums)):
    num = nums[i]

    if num > idx:
        for j in range(idx+1, num+1):
            stack.append(j)
            result.append('+')
        idx = num
    elif stack[-1] != num:
        print('NO')
        exit()
    stack.pop()
    result.append("-")

for i in result:
    print(i)
