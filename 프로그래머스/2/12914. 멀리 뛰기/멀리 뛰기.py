def fac(n):
    fact=1
    for i in range(1,n+1):
        fact=fact*i
    return fact


def solution(n):
    answer=0 # 총 가짓수
    maximum = n//2 if n%2==0 else n//2+1 # 2칸으로 갈 수있는 max 

    i= 0 if n%2==0 else 1 # 1의 갯수
    maxcount =maximum # 뛰는 횟수


    while i<=maxcount:
        if n%2==1 :
            answer=answer+fac(maxcount)//(fac(maxcount-i)*fac(i))

        else :
            answer=answer+fac(maxcount)//(fac(maxcount-i)*fac(i))

        maxcount=maxcount+1
        i=i+2

    return answer%1234567
