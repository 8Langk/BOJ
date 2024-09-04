def solution(n, cores):
    answer=1    
    process =0
    processed =0
    if n < len(cores):
        return 1
    
    else:
        n-=len(cores)
        left, right= 0, n*max(cores)
        while left<right:

            mid = (left+right)//2
            process=0
            for i in cores:
                process+= mid//i  
            if process>=n:
                right = mid
            else:
                left=mid+1 
        times = left
        for i in cores:
            processed+= (times-1)//i
        n-=processed
       

        for i in range(1,len(cores)+1):
            if times%cores[i-1]==0:
                n-=1

                if n==0:
                    answer=i
                    return answer
        
        
    return answer