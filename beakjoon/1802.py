# 종이접기
import sys

input = sys.stdin.readline


def paper_fold(paper):
    """
    종이접기 검사
    paper_status: 입력 받은 종이상태
    """
    N = len(paper)
    if N == 1:
        return True
    mid = N // 2
    for i in range(mid):
        if paper[i] == paper[N - (i + 1)]:  # 대칭으로 존재할수 없음
            return False
    return paper_fold(paper[:mid])
    pass


def solution():
    for _ in range(case := int(input())):
        if paper_fold(input().strip()):
            print("YES")
        else:
            print("NO")
    pass


if __name__ == "__main__":  # 실행되는 부분
    solution()
    pass
