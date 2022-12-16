#위장
def solution(clothes):
    answer=[]
    answer_sum=0
    types={cloth[1]:0 for cloth in clothes}
    for cloth in clothes:
        types[cloth[1]]+=1
    for i in types.values():
        answer.append(i+1)
    for i in answer:
        if answer_sum==0:
            answer_sum+=i
        else :answer_sum*=i
    return answer_sum-1