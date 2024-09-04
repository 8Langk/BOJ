a=input()

a=int(a)

count_right=a%10
sum=a//10+count_right
next_number=count_right*10+sum%10

count=1

while next_number!=a :
    count_right=next_number%10
    sum=next_number//10+count_right
    next_number=count_right*10+sum%10
    count+=1

print(count)

