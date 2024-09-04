def next_torn(t):
    if(t%2==0):
        return t//2
    else:
        return t//2+1


player, jimin_num, hansu_num = map(int,input().split())

match_round=0

    
while(player!=1):
    match_round+=1
    if(((jimin_num%2==1 and hansu_num%2==0) and jimin_num+1==hansu_num) or ((jimin_num%2==0 and hansu_num%2==1) and jimin_num==hansu_num+1)):      
        print(match_round)
        break
    else:
        jimin_num=next_torn(jimin_num)
        hansu_num=next_torn(hansu_num)

    if(player%2==0):
        player//2
    else: 
        player//2+1
            
        