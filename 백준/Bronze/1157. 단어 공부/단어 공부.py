word=input()
list_word_count = [0 for i in range(100)]


for i in range(len(word)):
    if(ord(word[i])>=97):
        list_word_count[ord(word[i])-32]+=1
    else :
        list_word_count[ord(word[i])]+=1

max=list_word_count[0]
alpha=0
checkSameWord=1
list[10000001]

for i in range (1,100):
    if max<list_word_count[i] :
        max=list_word_count[i]
        alpha=i
        checkSameWord=1

    elif(max==list_word_count[i]):
        checkSameWord=-1

if checkSameWord==-1:
    print('?')
else:
    print(chr(alpha))


