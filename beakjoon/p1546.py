
subjects = int(input())
score_list = list(map(int,input().split()))
newMax= max(score_list)
new_score_li=[]
for i in range(subjects):
    new_score_li.append(score_list[i]/newMax*100)
print(sum(new_score_li)/subjects)
