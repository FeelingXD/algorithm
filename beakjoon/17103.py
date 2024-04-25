# 골드바흐의 파티션
import sys

input = sys.stdin.readline
input_max=1_000_000

aristo=[0,0]+[1]*(input_max-2)
def create_aristo():
    global aristo
    for i in range(2,input_max):
        if aristo[i]:
            j=2
            while i*j<=input_max-1:
               aristo[i*j]=0
               j+=1 

def solution():
    global aristo
    create_aristo()
    
    for _ in range(test_case:=int(input())):
        tmp=int(input())
        partitions=0
        for i in range(2,tmp//2+1):
            if aristo[i] and aristo[tmp-i]:
                partitions+=1
        print(partitions) 
            
    pass


if __name__ == "__main__":  # 실행되는 부분
    solution()
    pass
