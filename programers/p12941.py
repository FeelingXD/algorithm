def solution(A,B):
    A=sorted(A)
    B=sorted(B)
    sum=0
    for i in range(len(A)):
        sum+=A[i] * B[len(B)-i-1]
    return sum