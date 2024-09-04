def solution(n):
    
    watermelon = '수박'
    answer = ''
    i=0
    
    while i<=n-1:
        j=i%2
        answer = answer + watermelon[j]
        i=i+1

    return answer