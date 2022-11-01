#M과 N이 주어질 때 M이상 N이하의 자연수 중 완전제곱수인 것을 
#모두 골라 그 합을 구하고 그 중 최솟값을 찾는 프로그램을 작성하시오.

fst = int(input())
sec = int(input())
num_list=[]

for num in range(fst,sec+1):
    if int(num**0.5)==num**0.5:
        num_list.append(num)

if len(num_list)!=0:
    print(sum(num_list))
    print(min(num_list))
else :
    print(-1)