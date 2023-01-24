# 정수 삼각형
def solution(triangle):
    return max(dp(triangle, [])[len(triangle)-1])


def dp(origin, arr):
    arr = origin.copy()
    for height in range(1, len(origin)):
        for idx in range(len(origin[height])):
            if idx == 0:
                arr[height][idx] += arr[height-1][idx]
            elif idx == len(origin[height])-1:
                arr[height][idx] += arr[height-1][len(arr[height-1])-1]
            else:
                arr[height][idx] += max(arr[height-1]
                                        [idx], arr[height-1][idx-1])
    return arr
