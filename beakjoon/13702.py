# 이상한 술집
import sys

input = sys.stdin.readline


def solution():
    N, K = map(int, input().split())  # 주전자 갯수, 친구들 수
    drinks = [int(input()) for _ in range(N)]
    drinks.sort()
    s, e = 0, drinks[-1]  # 초기값은 0 과 음료중 가장 큰값을 취해줌
    ans = 0

    while s <= e and N > 0 and K > 0:
        cnt = 0
        mid = (s + e) // 2 if (s + e) // 2 else 1
        for drink in drinks:
            cnt += drink // mid
        if cnt < K:  # 친구 모두에게 나눠주지 못 한경우
            e = mid - 1
        else:  # 모두 나눠준경우 갱신
            ans = max(ans, mid)
            s = mid + 1
    print(ans)
    pass


if __name__ == "__main__":  # 실행되는 부분
    solution()
    pass
