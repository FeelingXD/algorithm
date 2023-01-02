# 서로소를 활용한 사이클 판별
import sys
input = sys.stdin.readline
# 3 3
# 1 2
# 1 3
# 2 3


def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]


def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


v, e = map(int, input().split())  # 노드와 간선
parent = [0] * (v+1)  # 부모테이블의 초기화

for i in range(v+1):
    parent[i] = i

cycle = False

for i in range(e):
    a, b = map(int, input().split())
    if find_parent(parent, a) == find_parent(parent, b):
        cycle = True
        break
    else:
        union_parent(parent, a, b)

if cycle:
    print('cycled')
else:
    print('not cycled')