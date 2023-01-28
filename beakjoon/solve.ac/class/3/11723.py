import sys
input = sys.stdin.readline
n = int(input())
container = set()
for _ in range(n):
    order = input().split()
    if order[0] == 'add':
        container.add(int(order[1]))
    elif order[0] == 'remove':
        if int(order[1]) in container:
            container.remove(int(order[1]))
    elif order[0] == 'check':
        print(1 if int(order[1]) in container else 0)
    elif order[0] == 'toggle':
        if int(order[1]) in container:
            container.remove(int(order[1]))
        else:
            container.add(int(order[1]))
    elif order[0] == 'all':
        container = {_ for _ in range(1, 21)}
    elif order[0] == 'empty':
        container = set()
