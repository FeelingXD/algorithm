# 약수들의 합
import sys
input = sys.stdin.readline

def get_measures(n):
    measures=[]
    for i in range(1,int(n**(1/2))+1):
        if not n%i:
            if not i==n**(1/2)==int(n**(1/2)):
                measures.append(i)
                measures.append(n//i)
            else:
                measures.append(int(n**(1/2)))
    measures.sort()
    return measures
def is_perfect(mesures:list):
    if mesures[-1]==sum(mesures[:(len(mesures)-1)]):
        answer=f'{mesures[-1]} = '
        for  i in range(len(mesures)-1):
            if i!=len(mesures)-2:
                answer+=f'{mesures[i]} + '
            else:
                answer+=f'{mesures[i]}'
        return answer
    else:
        return f'{mesures[-1]} is NOT perfect.' 
    pass
def solution():
    while n:=int(input()):
        if n==-1:
            break
        print(is_perfect(get_measures(n)))
    pass
if __name__=="__main__":
    solution()
    pass