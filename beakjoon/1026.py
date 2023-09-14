# 보물
import sys
input = sys.stdin.readline

if __name__ == "__main__":
    n = int(input())
    A_list = list(map(int, input().split()))
    B_list = list(map(int, input().split()))
    answer = 0
    for a, b in zip(sorted(A_list), sorted(B_list, reverse=True)):
        answer += a*b
    print(answer)
