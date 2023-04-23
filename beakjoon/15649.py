# N과 M(1)
from itertools import combinations, permutations

N, M = map(int, input().split())

nums = [i for i in range(1, N+1)]

permu = list(permutations(nums, M))
for i in permu:
    print(*i)
