# 트리순회
n = int(input())
graph = {}

for _ in range(n):
    root, l, r = map(str, input().split())
    graph[root] = [l, r]


def preOrder(graph, start):
    print(start, end='')
    for i in graph[start]:
        if i == ".":
            continue
        preOrder(graph, i)


def inOrder(graph, start):
    l, r = graph[start]

    if l != '.':
        inOrder(graph, l)
    print(start, end="")
    if r != '.':
        inOrder(graph, r)


def postOrder(graph, start):
    for i in graph[start]:
        if i != '.':
            postOrder(graph, i)
    print(start, end='')


preOrder(graph, "A")
print()
inOrder(graph, "A")
print()
postOrder(graph, "A")
