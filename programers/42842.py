#카펫
def solution(brown, yellow):
    answer=[]
    carpets =brown +yellow
    sum=brown+yellow
    for i in range(3,int(sum/2)+1):
        j= sum/i
        
        if j!=int(j):
            continue
        if (i-2)*(j-2)==yellow:
            answer.append(int(i))
            answer.append(int(j))
            break
        
    if answer[0]<answer[1]:
            answer[0],answer[1]= answer[1],answer[0]
    return answer

solution(10,2)
print("🐍 File: programers/#test.py | Line: 18 | undefined ~ solution(12,2)",solution(10,2))


