from collections import deque

def solution(n, edge):
    answer = 0
    length_edge = len(edge)
    inf = -1
    vertex={i+1:[] for i in range(n)}
    di = [inf] * (n+1)
    
    for i in range(length_edge):
        a,b = edge[i]
        vertex[a].append(b)
        vertex[b].append(a)

    #초기설정
    q = deque([1])
    di[1]=0
    maxes= 0
    while q:
        node = q.popleft() #[1]

        for i in vertex[node]:
            #print(di, i)
            if di[i]==inf:
                di[i]=di[node]+1
                if maxes<di[i]:
                    maxes=di[i]
                    cnt=1
                elif maxes>=di[i]:
                    cnt+=1
                
                q.append(i)
            
        answer= cnt
            
    
    return answer