import sys

n = int(input())
dic= set(input() for i in range(n))

dic=list(dic)

dic.sort()
dic.sort(key=lambda x: len(x))

#sort(dic,len(dic))

print(*dic, sep='\n')



