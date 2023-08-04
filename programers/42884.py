# 단속 카메라
def solution(routes):
    answer = 0
    routes.sort(key=lambda x: (x[1], x[0]))
    tmp = -99999
    for route in routes:
        if not route[0] <= tmp <= route[1]:
            answer += 1
            tmp = route[1]
    return answer
