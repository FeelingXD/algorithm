# 주몽
import sys

input = sys.stdin.readline


def solution():
    n = int(input())
    target = int(input())
    armors = sorted(list(map(int, input().split())))
    l, r = 0, len(armors) - 1
    ans = 0
    while l < r:
        tmp = armors[l] + armors[r] if l != r else armors[l]
        if tmp == target:
            ans += 1

        if tmp < target:
            l += 1
        else:
            r -= 1
        pass
    print(ans)


if __name__ == "__main__":  # 실행되는 부분
    solution()
    pass
