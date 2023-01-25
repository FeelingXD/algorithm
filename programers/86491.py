# 최소 직사각형
def solution(sizes):
    return max(sorted(sizes, key=lambda x: -max(x[0], x[1]))[0])*min(sorted(sizes, key=lambda x: -min(x[0], x[1]))[0])
