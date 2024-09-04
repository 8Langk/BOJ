def solution(name):
    answer = 0
    name_len = len(name)
    min_move = name_len-1
    
    for i in range(name_len):
        answer+= min([ord(name[i])-ord('A'), 26-(ord(name[i])-ord('A'))])
        
        end = i+1
        while(end < name_len and name[end]=='A'):
            end+=1
        
        min_move = min([min_move, 2*i+(name_len-end), 2*(name_len-end)+i])    
    answer+= min_move
        
        #print(answer)
    return answer

#b,c,d,e,f,g,h,i,j