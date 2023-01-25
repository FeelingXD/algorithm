# 조합 도출
# python 내장기능
from itertools import product, permutations, combinations


def my_combiantion(arr: list, n: int):
    result = []
    if n == 0:
        return [[]]

    for i in range(0, len(arr)):
        elem = arr[i]
        rest_arr = arr[i+1:]
        for C in my_combiantion(rest_arr, n-1):
            result.append([elem]+C)
    return result


items = ['1', '2', '3', '4', '5']
# print("🐍 File: Math/Combination.py | Line: 6 | undefined ~ list(permutations(items, 2))",
#       list(permutations(items, 2)))
# print("🐍 File: Math/Combination.py | Line: 9 | undefined ~ list(combinations(items, 2))",
#       list(combinations(items, 2)))

print("🐍 File: Math/Combination.py | Line: 21 | undefined ~ my_combiantion(items,2)",
      my_combiantion(items, 3))
