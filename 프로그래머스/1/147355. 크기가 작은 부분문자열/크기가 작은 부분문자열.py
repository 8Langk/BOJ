def solution(t, p):
    answer = 0
    plen=len(p)
    
    cmparr=[]
    
    for i in range(len(t)):
        if(len(t)-i<plen):
            break
        cmparr.append(t[i:i+plen])
    for i in cmparr:
        if int(p)>=int(i):
            answer+=1
    return answer