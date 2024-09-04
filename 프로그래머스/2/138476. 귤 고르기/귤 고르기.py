def solution(k, tangerine):
    aaa = [0 for i in range(max(tangerine)+1)]
    answer = 0

    for i in tangerine:
        aaa[i]=aaa[i]+1

    c= sorted(aaa, reverse=True)

    for i in c:
        if k-i<=0:
            answer=answer+1
            break
        k=k-i
        answer=answer+1

    return answer