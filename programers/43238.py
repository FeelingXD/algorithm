# 입국심사
def solution(n, times):
    answer = 10e9
    mt = max(times)
    l, r = 1, mt * n
    while l <= r:
        mid = (l + r) // 2
        cnt = 0

        for time in times:
            cnt += mid // time

        if cnt >= n:
            answer = mid
            r = mid - 1
        else:
            l = mid + 1

    return answer
