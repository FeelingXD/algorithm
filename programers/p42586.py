# 큐와 스택 / 큐이용
def solution(progresses, speeds):
    time=1 #min
    count=0
    answer=[]
    while(len(progresses)!=0):
        if(progresses[0]+speeds[0]*time>=100):
            progresses.pop(0)
            speeds.pop(0)
            count+=1
        else:
            if(count >0):
                answer.append(count)
                count=0
            else:
                time+=1
    answer.append(count)
    return answer