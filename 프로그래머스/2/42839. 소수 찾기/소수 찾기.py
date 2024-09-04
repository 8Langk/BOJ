from itertools import * 

def solution(numbers):
    answer = 0
    a=set()
    is_prime=1
    
    for i in range(1, len(numbers)+1): #모든 경우의 수 만들기
        a|=set(map(int, map(''.join, permutations(numbers,i))))
    a-={0,1} #0, 1 빼기

    for i in a:
        is_prime=1
        for j in range(2,int(i**(1/2))+1):
            if i%j==0:
                is_prime=0
                break
        if is_prime==1:
            answer+=1
            
        
    return answer