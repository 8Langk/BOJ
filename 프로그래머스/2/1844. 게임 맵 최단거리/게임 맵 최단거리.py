a=[]
from collections import deque

def BFS(maps,m,n):
    total_cost=1
    sign = [(-1,0),(1,0),(0,-1),(0,1)]
    queue = deque()
    queue.append([0,0])
    while queue:
        x_1, y_1= queue.popleft()
        for i in sign:
            x=x_1+i[0]
            y=y_1+i[1]
            
            if 0<=x<m and 0<=y<n:
                if maps[x][y]==1:
                    maps[x][y]=maps[x_1][y_1]+1
            #DFS(maps,total_cost,x,y,m,n)
                    queue.append([x,y])
            if x_1 == m-1 and y_1 ==n-1 :
                answer = maps[x_1][y_1]
                return answer
    
    return -1 
def solution(maps):
    answer = 0
    m= len(maps)
    n= len(maps[0])
    
    answer = BFS(maps,m,n)
    
    print(answer)
    return answer