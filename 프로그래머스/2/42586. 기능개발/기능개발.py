def solution(progresses, speeds):
    answer=[]
    days =1
    cnt=0
    
    while len(progresses):
        if progresses[0]+days*speeds[0]>=100:
            progresses.remove(progresses[0])
            speeds.remove(speeds[0])
            cnt+=1
        else :
            if cnt > 0 :
                answer.append(cnt)
                cnt=0
            days+=1
    answer.append(cnt)
                
    return answer