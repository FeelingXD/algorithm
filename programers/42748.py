# K 번째 수
def solution(array, commands):
    #commands =(start,end,index)
    answer = []
    for command in commands:
        answer.append(sorted(array[command[0]-1:command[1]])[command[2]-1])
    return answer
