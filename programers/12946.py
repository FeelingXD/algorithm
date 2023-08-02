def solution(n):
    answer = []
    hanoi(n, 1, 2, 3, answer)
    return answer


def hanoi(n, st, by, to, li):
    if n == 1:
        li.append([st, to])
    else:
        hanoi(n-1, st, to, by, li)
        li.append([st, to])
        hanoi(n-1, by, st, to, li)
