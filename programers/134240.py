# 푸드 파이트 대회
def solution(food):
    prestr = ""
    for i in range(1, len(food)):
        tmp = food[i]//2
        while tmp:
            prestr += str(i)
            tmp -= 1
    answer = [prestr, prestr[::-1]]
    return "0".join(answer)
