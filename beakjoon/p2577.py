#숫자의 개수
a= int(input())
b= int(input())
c= int(input())
k_list = str(a*b*c)
print(k_list)
for i in range(10):
  print(k_list.count(str(i)))
