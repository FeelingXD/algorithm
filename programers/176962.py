# 과제수
def subtract_times(time1, time2):
    # 시간을 시간 단위와 분 단위로 변환
    hours1, minutes1 = map(int, time1.split(':'))
    hours2, minutes2 = map(int, time2.split(':'))

    # 시간과 분을 분 단위로 합산
    total_minutes_time1 = hours1 * 60 + minutes1
    total_minutes_time2 = hours2 * 60 + minutes2

    # 두 시간의 차이 계산
    time_difference = total_minutes_time1 - total_minutes_time2

    return time_difference


def solution(plans):
    answer = []
    plans = [(name, st, int(duration)) for name, st, duration in plans]
    plans.sort(key=lambda x: x[1])  # 시작시간으로 정렬하기
    # left queue

    left = []
    left_time = 0

    for i in range(len(plans)):
        name, st, pt = plans[i]
        while left and 0 <= left_time:  # 멈춰둔게있으면
            _name, _pt = left.pop()  # 최근에추가한걸 뺌
            if left_time >= _pt:
                left_time -= _pt
                answer.append(_name)
            else:  # 자투리시간이 모자른경우
                left.append((_name, _pt-left_time))
                break
        left.append((name, pt))

        if i < len(plans)-1:
            n_s = plans[i+1][1]  # 다음시작시간
            left_time = subtract_times(n_s, st)

    while left:
        answer.append(left.pop()[0])
    return answer
