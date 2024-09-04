import sys
n = int(sys.stdin.readline())


data = list(map(int, sys.stdin.readline().split()))
k= {i : 0 for i in data}


m = int(input())

quest = list(map(int, sys.stdin.readline().split()))

for i in range(m):
    if quest[i] in k:
        print("1")
    else :
        print("0")