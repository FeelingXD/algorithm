# 문자열 내 마음대로 정렬하기
def solution(strings, n):
    new_strings = []
    for i in strings:
        new_strings.append(i[n]+i)
    new_strings.sort()

    return [i[1:] for i in new_strings]
