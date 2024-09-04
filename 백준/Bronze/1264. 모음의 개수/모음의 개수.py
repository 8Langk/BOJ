
sentence=''

while(True):
    count=0
    sentence = input()
    for i in range (len(sentence.strip())):
        if(sentence[i]=='a' or sentence[i]=='A' or sentence[i]=='e' or sentence[i]=='E' or sentence[i]=='i' or sentence[i]=='I' or sentence[i]=='o' or sentence[i]=='O' or sentence[i]=='u' or sentence[i]=='U'):
            count+=1
    if(sentence=='#'):
        break
    print(count)     

    