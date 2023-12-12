import sys
input =sys.stdin.readline

def back_tracking(score):
    global answer
    global energy_list
    if len(energy_list)==2:
        answer=max(answer,score)
        return
    else:
        for i in range(1,len(energy_list)-1):
            c_s=energy_list[i-1]*energy_list[i+1]
            v=energy_list.pop(i)
            back_tracking(score+c_s)
            energy_list.insert(i,v)
            
def solution():
    global energy_list
    global answer
    answer=0
    n=int(input())
    energy_list=list(map(int,input().split()))
    back_tracking(0)
    print(answer)
    pass
if __name__=="__main__": # 실행되는 부분
    solution()
    pass