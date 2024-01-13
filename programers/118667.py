# 두 큐 합 같게 만들기
from collections import deque
def solution(queue1, queue2):
    q1,q2=deque(queue1),deque(queue2)
    
    current_q1_result=sum(q1)
    current_q2_result=sum(q2)
    
    target=(current_q1_result+current_q2_result)/2
    cnt=0
    for _ in range(len(q1)*3):
        
        if current_q1_result==current_q2_result:
            return cnt
        
        elif current_q1_result>target:
            v=q1.popleft()
            q2.append(v)
            
            current_q1_result-=v
            current_q2_result+=v
        else:
            v=q2.popleft()
            q1.append(v)
            
            current_q2_result-=v
            current_q1_result+=v
        
        cnt+=1 
    return -1