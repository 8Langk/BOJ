def solution(brown, yellow):
    answer = []
    total = brown + yellow

    # total = width * height
    
    # width-2 * height-2 = innerRec
    # total - innerrec(yellow) = brown
    for height in range(1, brown) : 
        if total%height ==0:
            width = total//height
            if (width-2)*(height-2) == yellow :
                answer.append([width, height])
                break
                
    return answer[0]