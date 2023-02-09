# 블랙잭
from itertools import combinations
import sys
input = sys.stdin.readline

cnt, target = map(int, input().split())
cards = list(map(int, input().split()))
print(max([sum(i) for i in combinations(cards, 3) if sum(i) <= target]))
