def solution(n, times):
    maximum = max(times)*n
    
    right= maximum
    left=0
    
    while left<right:
        sum=0
        mid = (left + right)//2
        
        for i in times:
            sum+=mid//i
        
        if sum>=n:
            right = mid
        else :
            left= mid+1
        #print(left, mid, right)
    
    

    return right
        