num =int(input())

score =[]
average = 0

score.append(list(map(int,input().split())))
max_score =max(score[0])

for i in range (len(score[0])):
    
    score[0][i]=score[0][i]/max_score*100
    average += score[0][i]

print(average/len(score[0]))