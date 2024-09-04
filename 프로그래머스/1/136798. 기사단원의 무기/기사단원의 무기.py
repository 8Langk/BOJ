def solution(number, limit, power):
    yaksu = [0 for i in range(number+1)]
    answer= 0

    for i in range(1,number+1):
        cnt=0
        for j in range(1,(int)(i**(1/2))+1):
            if i%j==0:
                if j==i/j:
                    cnt=cnt+1
                else:
                    cnt=cnt+2
        yaksu[i]=cnt

    for i in range(1, len(yaksu)):
        if yaksu[i]>limit:
            answer=answer+power
        else :
            answer=answer+yaksu[i]

        
    return answer