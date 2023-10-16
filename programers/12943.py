# 콜라츠 추측
def dfs(num, d):
    if num == 1:
        return d
    else:
        if d >= 500:
            return -1
        else:
            return dfs(num//2, d+1) if num % 2 == 0 else dfs(3*num+1, d+1)


def solution(num):
    return dfs(num, 0)
