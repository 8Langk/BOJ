import heapq

def solution(scoville, K):
    answer=0

    heapq.heapify(scoville)

    while(scoville):
        if scoville[0]>=K:
            return answer

        if len(scoville)>1:
            mini = heapq.heappop(scoville)
            second_mean = heapq.heappop(scoville)
            nextScoville=mini+2*second_mean
            heapq.heappush(scoville,nextScoville)
            answer+=1

        else : 
            answer=-1
            return answer
