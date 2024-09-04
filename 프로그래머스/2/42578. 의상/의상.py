def solution(clothes):
    answer = 1
    
    clothes_hash = {}
    
    for i in range(len(clothes)):
        if clothes[i][1] not in clothes_hash:
            clothes_hash[clothes[i][1]] = [0]
            clothes_hash[clothes[i][1]].append(clothes[i][0])
        else :
            clothes_hash[clothes[i][1]].append(clothes[i][0])
            
    for clothes in clothes_hash:
        answer*= len(clothes_hash[clothes])

    answer-=1 # 전부 0일때.
    
    return answer