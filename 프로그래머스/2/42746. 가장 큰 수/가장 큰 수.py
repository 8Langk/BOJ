def solution(numbers):
    answer = ''
    numbers=[str(i) for i in numbers]
    num = sorted(numbers, key=lambda x : x*3,reverse = True)
    
    for i in range(len(num)):
        if num[0] == "0":
            return "0"
        answer+=num[i]
    
    return answer
