# 서로소
# 6 4
# 1 4
# 2 3
# 2 4
# 5 6

import sys
input = sys.stdin.readline
# 특정 원소가 속한 집합을 찾기


def find_parent(parent, x):
    # 루트 노드가 아니라면, 루트 노드를 찾을 때까지 재귀적을 호출
    if parent[x] != x:
        return find_parent(parent, parent[x])
    return x


def find_parent(parent, x):
    if parent[x] != x:
        return find_parent(parent, parent[x])
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

for i in range(e):
    a, b = map(int, input().split())
    union_parent(parent, a, b)
#
print('속한 집합', )
for i in range(1, v+1):
    print(find_parent(parent, i), end=' ')
print()

print('부모')
for i in range(1, v+1):
    print(parent[i], end=' ')
