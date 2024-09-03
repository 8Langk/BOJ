import sys
dic= {}

n, m = map(int,sys.stdin.readline().split())

for i in range(n):
    word=sys.stdin.readline().strip('\n')
    if word not in dic:
        dic[word]=1
    else:
        dic[word]+=1

dic= dict(sorted(dic.items(), key=lambda x: (-x[1],-len(x[0]),x[0])))
dic=[i[0] for i in dic.items() if len(i[0])>=m]

for i in dic:
    print(i)