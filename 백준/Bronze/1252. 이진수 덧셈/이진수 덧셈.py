binaryCode1, binaryCode2= map(int,input().split())

newBinaryCode=[0 for i in range (81)]
next_number=binaryCode1+binaryCode2
last_num=0

if(binaryCode1==binaryCode2==0):
    print('0')
    exit()
    
for i in range (len(newBinaryCode)):
    newBinaryCode[len(newBinaryCode)-i-1]=next_number%10
    next_number=next_number//10



for i in range (len(newBinaryCode)):
    if(newBinaryCode[len(newBinaryCode)-i-1]>=1):
        last_num=len(newBinaryCode)-i-1
        
    if(newBinaryCode[len(newBinaryCode)-i-1]>=2):
        if (newBinaryCode[len(newBinaryCode)-i-1]%2==0):
            newBinaryCode[len(newBinaryCode)-i-1]=newBinaryCode[len(newBinaryCode)-i-1]%2
            newBinaryCode[len(newBinaryCode)-i-2]+=1
            
        else:
            newBinaryCode[len(newBinaryCode)-i-1]=1
            newBinaryCode[len(newBinaryCode)-i-2]+=1
            
    
    
print(*newBinaryCode[last_num:len(newBinaryCode)], sep='')