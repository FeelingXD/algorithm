# p name =Yangjojang of The Year

count_case=int(input())
answer=[0]*count_case
for case in range(count_case):
    value_count=int(input())
    dic={} #univ status name:consume
    for value_count in range(value_count):
        univ_name, consume = input().split()
        dic[univ_name]=int(consume)
    answer[case]=[k for k,v in dic.items() if v ==max(dic.values())][0]
print('\n'.join(answer))