# 연속된 부분 수열의 합
def solution(sequence, k):
    answer = []
    left,right=0,1
    max_seq=len(sequence)+1
    prefix_sum=[0]*(max_seq)
    tmp=0
    for i in range(0,len(sequence)):
        tmp+=sequence[i]
        prefix_sum[i+1]=tmp
    while left<right and right<len(prefix_sum):
        current_v=(prefix_sum[right]-prefix_sum[left])
        if current_v==k:
            answer.append((left,right-1))
            right+=1
        elif k<current_v:
            left+=1
        else:
            right+=1
    answer.sort(key=lambda x:(x[1]-x[0]))
    return answer[0]
    
