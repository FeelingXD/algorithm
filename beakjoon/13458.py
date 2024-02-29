# 시험 감독
import sys

input = sys.stdin.readline


def solution():
    N = int(input())
    candidates = list(map(int, input().split()))
    B, C = map(int, input().split())  # 총감독과 부감독이 감시하는 응시자 수들
    ans = len(candidates)  # 총감독은 각 반마다 한명씩 있어야한다.
    candidates = list(map(lambda x: x - B, candidates))
    for unchecked in candidates:
        if unchecked <= 0:  # 총감독이 커버할수 있는 인원수가 0이하인경우 패스
            continue
        else:
            ans = ans + unchecked // C + 1 if unchecked % C else ans + unchecked // C
    print(ans)
    pass


if __name__ == "__main__":  # 실행되는 부분
    solution()
    pass
