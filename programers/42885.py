# 최대 2명씩 밖에 제일무거운사람 +작은사람
from collections import deque
def solution(people:list,limit:int):
    answer=0
    people.sort()
    people=deque(people)
    while people:
        if len(people)==1:
            answer+=1
            break
        
        elif people[0]+people[-1]<=limit :
            people.pop()
            people.popleft()
            answer+=1
       
        else :
            people.pop()
            answer+=1
    return answer
print(solution(	[70, 80, 50], 100))