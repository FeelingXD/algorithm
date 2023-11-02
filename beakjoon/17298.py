# 오큰수
import sys
input = sys.stdin.readline

if __name__ == "__main__":
    n = int(input())
    li = list(map(int, input().split()))
    answer = [-1]*n
    stack = []
    for v in range(0, n):
        while stack and li[stack[-1]] < li[v]:
            answer[stack.pop()] = li[v]
        stack.append(v)
    print(*answer)
    pass
