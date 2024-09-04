def solution(citations):
    answer = 0
    cnt=0
    #정렬하고, 음.. 순회하면서 5번일 때 5회, 3번일때 3편이상.... 이면
    nonmun_gaetsu = len(citations)
    citations.sort()
    
    """if citations[0]==0:
        return 0
    
    for i in range(nonmun_gaetsu,0,-1) :
        cnt=0
        for j in citations:
            if j >= i: #0, 
                cnt+=1
                if cnt==i:
                    return i
            else : break
    return nonmun_gaetsu        """ 
    """print(citations)
    for i in range(1, nonmun_gaetsu+1):
        if i <= citations[i-1]:
            print(i)
            #1 < 6 , 2<5, 3<3
        else:
            return i-1
            break
    return i
            """
    for i in range(nonmun_gaetsu):
        if citations[i] >=nonmun_gaetsu-i:
            return nonmun_gaetsu-i

    return citations[0]
            
        #[0,1,2,5,6]
        
        #[10,9,8,7,6] 6편 이상 6개 x 
        #[6,5,2,1,0] 2
        #[6,5,4,4,0] 
        #[7,5,1,1,0] -> 2이상인게 2개
   