# 오리
import sys
input = sys.stdin.readline

duck_sound = "quack"
duck = input().strip()
visited = [False for i in range(len(duck))]
peak = 0


def find(start):
    global peak
    first = True
    j = 0
    for i in range(start, len(duck)):
        if duck[i] == duck_sound[j] and not visited[i]:
            visited[i] = True
            if duck[i] == 'k':
                if first:
                    peak += 1
                    first = False
                j = 0
                continue
            j += 1
    pass


for i in range(len(duck)):
    if duck[i] == 'q' and not visited[i]:
        find(i)
    pass
if len(duck) % 5 != 0:
    print(-1)
    exit()
print(peak if all(visited) and peak != 0 else -1)
