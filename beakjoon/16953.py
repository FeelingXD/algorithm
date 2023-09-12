# A → B
import sys
from collections import deque
input = sys.stdin.readline


def bfs(start_number, target_number):
    q = deque()
    q.append((start_number, 1))
    answer = -1
    while q:
        n, d = q.popleft()
        if n == target_number:
            answer = d
        else:
            if 2*n <= target_number:
                q.append((2*n, d+1))
            n_plus1 = int(str(n)+"1")
            if n_plus1 <= target_number:
                q.append((n_plus1, d+1))
    return answer


if __name__ == "__main__":
    start_number, target_number = map(int, input().split())
    print(bfs(start_number, target_number))
