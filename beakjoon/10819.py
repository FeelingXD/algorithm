# 차이를 최대로
from itertools import permutations
import sys
input = sys.stdin.readline

n = int(input())
max_result = 0
numbers = list(map(int, input().split()))


def calcul(nums):
    result = 0
    for i in range(1, len(nums)):
        result += abs(nums[i-1]-nums[i])
    return result


for i in list(permutations(numbers, n)):
    max_result = max(max_result, calcul(i))

print(max_result)
