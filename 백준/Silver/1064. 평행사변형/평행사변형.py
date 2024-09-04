rectangle=[]


x_1,y_1,x_2,y_2,x_3,y_3 = map(int,input().split())

if (x_1-x_2)*(y_2-y_3)==(y_1-y_2)*(x_2-x_3):
    print('-1.0')
    exit()
line_1 = pow(pow((x_1-x_2),2)+pow((y_1-y_2),2),1/2) 
line_2 = pow(pow((x_2-x_3),2)+pow((y_2-y_3),2),1/2)
line_3 = pow(pow((x_3-x_1),2)+pow((y_3-y_1),2),1/2)

rectangle.append(2*(line_1+line_2))
rectangle.append(2*(line_2+line_3))
rectangle.append(2*(line_3+line_1))

max=rectangle[0]
min=rectangle[0]

for i in range (0,3):
    if max<rectangle[i]:
        max=rectangle[i]
    
    if min>rectangle[i]:
        min=rectangle[i]

print(max-min)