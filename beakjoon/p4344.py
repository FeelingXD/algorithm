def avrage(list):
    return (sum(list)-list[0])/list[0]
def Who_over_average(list):
    over_avrage_student=0
    for i in range(1,len(list)):
        if list[i]>avrage(list):
            over_avrage_student+=1
    return over_avrage_student/list[0]
case = int(input())
for i in range(case):
    s_list = list(map(int,input().split()))
    print('{0:.3f}%'.format((Who_over_average(s_list)*100)))
