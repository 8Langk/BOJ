def comparAB(a, b):
    cnt = 0
    length = min(len(a), len(b))
    for i in range(length):
        if a[i]==b[i]:
            cnt+=1
        else : break
    return cnt
            
n = int(input())
a = [input() for _ in range(n)]
cnt=[0]*n


b= sorted(list(enumerate(a)),key= lambda x : x[1])

for i in range(n-1):
    count = comparAB(b[i][1],b[i+1][1])
    cnt[b[i][0]]=max(cnt[b[i][0]], count)
    cnt[b[i+1][0]]=max(cnt[b[i+1][0]], count)

maxcount = max(cnt)
first=0

for i in range(n):
    if first==0:
        if cnt[i]==maxcount:
            first=a[i]
            print(a[i])
            pre = a[i][:maxcount]
    else:
        if cnt[i]==maxcount and a[i][:maxcount]==pre:
            print(a[i])
            break