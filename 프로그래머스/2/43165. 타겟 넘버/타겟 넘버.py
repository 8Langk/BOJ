answer=0

def DFS(idx, hap, target, numbers, number):
    global answer
    hap += number
    if (idx+1)==len(numbers):
        if hap == target:
            answer+=1
        return
    DFS(idx+1,hap, target, numbers, numbers[idx+1])
    DFS(idx+1,hap, target, numbers, -numbers[idx+1])
    return 

def solution(numbers, target):
    node = []
    node2 =[]
    

    DFS(0, 0, target, numbers,numbers[0])
    DFS(0, 0, target, numbers, -numbers[0])

    return answer