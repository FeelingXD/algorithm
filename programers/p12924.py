def solution(n):
    mid=n//2+1
    answer=1 # 본인값 최소 1개이상
    for str in range(1,mid):
        val=0
        for end in range(str,mid+1):  
            val+=end
            if val == n:
                answer +=1
                break
            if val > n :
                break
    return answer