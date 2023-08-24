# 잃어버린 괄호
import sys
from functools import reduce
input = sys.stdin.readline

li = list(map(str, input().strip().split("-")))
prefix_li = []
for va in li:
    prefix_li.append(sum(list(map(int, va.split("+")))))
print(prefix_li[0]) if len(prefix_li) == 1 else print(
    reduce(lambda x, y: x-y, prefix_li[1:], prefix_li[0]))
