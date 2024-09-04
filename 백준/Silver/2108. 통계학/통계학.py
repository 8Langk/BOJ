import math
import sys
n = int(sys.stdin.readline())
numbers=[]

for i in range(n):
    numbers.append(int(sys.stdin.readline()))

numbers.sort() #정렬


count_num={}

for i in numbers: #각 원소 별 개수 dictionary
    if i not in count_num:
        count_num[i]=1
    else:
        count_num[i]+=1

arthi_avg = round(sum(numbers)/n)

max_count = max(count_num.values())

print(arthi_avg) #산술 평균
print(numbers[n//2]) #중앙값
cnt=0

for i in count_num: #최빈값
    if count_num[i]==max_count:
        cnt+=1
        maxx=i
        if(cnt==2):
            print(maxx)
            break
    if i==list(count_num.keys())[-1]:
        print(maxx)
            

print(numbers[n-1] - numbers[0])