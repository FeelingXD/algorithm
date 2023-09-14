# 보물
import sys
input = sys.stdin.readline

if __name__ == "__main__":
    n = int(input())
    A_list = sorted(list(map(int, input().split())))
    B_list = list(map(int, input().split()))
    answer = 0

    for i in range(n):
        max_B = max(B_list)
        answer += A_list[i] * B_list[B_list.index(max_B)]
        B_list.remove(max_B)

    print(answer)
