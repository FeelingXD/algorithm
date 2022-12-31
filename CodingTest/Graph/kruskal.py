# 크루스칼알고리즘
# 최소신장트리
def find_parent(parent, x):
    if parent[x] != x:
        return find_parent(parent, parent[x])
    return parent[x]
