# 전구와 스위치
import sys

input = sys.stdin.readline


def use_switch(cur, tar):
    cnt = 0
    for i in range(1, n := len(cur)):
        if cur[i - 1] == tar[i - 1]:
            continue
        else:
            for j in range(i - 1, i + 2):
                if j < n:
                    cur[j] = 1 - cur[j]
            cnt += 1
        pass
    return 10e9 if cur != tar else cnt


def solution():
    ans = -1
    N = int(input())
    current = list(map(int, list(input().rstrip())))
    target = list(map(int, list(input().rstrip())))
    ans = use_switch(current[:], target)
    current[0] = 1 - current[0]
    current[1] = 1 - current[1]
    ans = min(use_switch(current[:], target) + 1, ans)
    print(ans if ans != 10e9 else -1)
    pass


if __name__ == "__main__":  # 실행되는 부분
    solution()
    pass
