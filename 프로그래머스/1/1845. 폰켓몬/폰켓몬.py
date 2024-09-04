def solution(nums):
    answer = 0
    n=len(nums)
    if len(set(nums))<=n//2:
        answer=len(set(nums))
    else:
        answer = n//2
    
    
    return answer