from collections import deque 
def solution(people, limit):
    answer=0
    people.sort()
    #deq = deque(people)
    
    '''while(deq):
        tmp_limit=limit
        tmp_limit-=deq.pop()
        if deq and (deq[0]<=tmp_limit) :
            tmp_limit-=deq.popleft()
                
        answer+=1'''
    a=0
    b=len(people)-1
    
    while a<=b:
        if people[a] + people[b] <=limit:
            a+=1
        b-=1
        answer+=1
    
    return answer