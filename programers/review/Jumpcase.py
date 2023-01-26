cnt = 0


def solution(n: int, k: int):  # n target #k=limit
    global cnt
    backTracking(n, k, 0, 0)
    return cnt % int(1e9+7)


def backTracking(target, limit, cur, last_value):
    global cnt
    if target == cur:
        cnt += 1
        return
    for i in range(1, limit+1):
        if i == last_value:
            continue
        if target < cur+i:
            break
        else:
            backTracking(target, limit, cur+i, i)


print("🐍 File: review/Jumpcase.py | Line: 21 | undefined ~ solution(5,3)", solution(3, 3))
