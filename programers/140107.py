def solution(k, maxnum):
    sum = 0
    for num in range(0, maxnum+1, k):
        y = int((maxnum*maxnum-num*num)**(1/2))
        sum += (y//k+1)
    return sum
