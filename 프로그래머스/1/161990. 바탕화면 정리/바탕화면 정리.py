def solution(wallpaper):
    answer=[]

    minX=50
    minY=50
    maxX=0
    maxY=0

    for i in range(len(wallpaper)):
        for j in range (len(wallpaper[i])):
            if wallpaper[i][j]=="#":
                if(minX>i) : minX=i
                if(maxX<i) : maxX=i
                if(minY>j) : minY=j
                if(maxY<j) : maxY=j

    answer=[minX,minY,maxX+1,maxY+1]
    
    return answer