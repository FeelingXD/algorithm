# 알록달록 앵무새
import sys
from itertools import product
input = sys.stdin.readline


f = set(input().split())
m = set(input().split())
parents = f | m
for per in sorted(product(parents, repeat=2), key=lambda x: (x[0], x[1])):
    print(*per)
