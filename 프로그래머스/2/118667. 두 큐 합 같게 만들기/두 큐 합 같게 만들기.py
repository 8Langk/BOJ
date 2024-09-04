def sum(queue):
    sumq=0
    for i in queue:
        sumq+=i
    return sumq

def solution(queue1, queue2):

    cnt=0
    sumq1= sum(queue1)
    sumq2= sum(queue2)
    indexq1=0
    indexq2=0
    balance = sumq1+sumq2 
    maxi = 3*len(queue1)
    if balance%2==1:
        return -1

 
    while True:
        if cnt>maxi:
            cnt=-1
            break

        if sumq1<sumq2:
            tmp = queue2[indexq1]
            queue1.append(tmp)
            indexq1+=1
            sumq1+=tmp
            sumq2-=tmp
            cnt+=1
            
        elif sumq1==sumq2:
            break
        
        else:
            tmp=queue1[indexq2]
            queue2.append(tmp)
            indexq2+=1
            sumq1-=tmp
            sumq2+=tmp
            cnt+=1

    return cnt
