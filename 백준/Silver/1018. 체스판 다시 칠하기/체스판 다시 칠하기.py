a ,b = map(int,input().split())

chess_list =[]
fucking_list=[[0 for i in range (8)]for j in range (8)]


list_min_8_8_w=[]
list_min_8_8_b=[]

count_w=0
count_b=0
min_w=[]
min_b=[]

r=0
c=0

fu_row=0
fu_col=0

for i in range (a):
    chess_list.append(list(input()))


while True:
    fu_col=0
    fu_row=0
    
    for i in range (r,r+8):
        for j in range(c,c+8):
            fucking_list[fu_row][fu_col]=chess_list[i][j]
            fu_col+=1
           
        fu_col=0
        fu_row+=1

    #
    count_w=0
    count_b=0
    
    for i in range (len(fucking_list)): #W부터 시작
        if(i%2==0):
            for j in range(len(fucking_list[i])):
                if(j%2==0):
                    if(fucking_list[i][j]!='W'):
                        count_w+=1
                else:
                    if(fucking_list[i][j]!='B'):
                        count_w+=1
        else:
            for j in range(len(fucking_list[i])):
                if(j%2==0):
                    if(fucking_list[i][j]!='B'):
                        count_w+=1
                else:
                    if(fucking_list[i][j]!='W'):
                        count_w+=1

    for i in range (len(fucking_list)): #B부터 시작
        if(i%2==0):
            for j in range(len(fucking_list[i])):
                if(j%2==0):
                    if(fucking_list[i][j]!='B'):
                        count_b+=1
                else:
                    if(fucking_list[i][j]!='W'):
                        count_b+=1
        else:
            for j in range(len(fucking_list[i])):
                if(j%2==0):
                    if(fucking_list[i][j]!='W'):
                        count_b+=1
                else:
                    if(fucking_list[i][j]!='B'):
                        count_b+=1

    min_w.append(count_w)
    min_b.append(count_b)

    c+=1
    if(c+8>b): 
        r+=1
        c=0
    if(r+8>a):
        break
        

print(min(min(min_w),min(min_b)))
