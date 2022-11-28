def solution(number):
    answer=number+1
    while bin(answer).count('1')!=bin(number).count('1'):
        answer+=1
    return answer