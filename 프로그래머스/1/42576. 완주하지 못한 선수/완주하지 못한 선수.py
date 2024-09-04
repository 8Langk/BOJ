def solution(participant, completion):
    answer = ''
    
    com ={}
    
    for i in participant:
        if i not in com:
            com[i]=1
        else :
            com[i]+=1
    

    for i in completion:
        if i in com:
            com[i]-=1
        if com[i]==0:
            del(com[i])

    answer=list(com.keys())[0]    
    return answer