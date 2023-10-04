# 풍선 터뜨리기
import sys
from collections import deque
input = sys.stdin.readline


if __name__ == "__main__":
    n = int(input())
    q = deque()
    answer = []
    for i, v in enumerate(list(map(int, input().split())), 1):
        q.append((i, v))
    while q:
        i, v = q.popleft()
        answer.append(i)
        if q:
            if 0 < v:
                for _ in range(v-1):
                    q.append(q.popleft())
            else:
                for _ in range(abs(v)):
                    q.appendleft(q.pop())
    print(*answer)
