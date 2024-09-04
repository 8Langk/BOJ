def percent_team_win(teamName,yeonduName):
    l=teamName.count('L')+yeonduName.count('L')
    o=teamName.count('O')+yeonduName.count('O')
    v=teamName.count('V')+yeonduName.count('V')
    e=teamName.count('E')+yeonduName.count('E')
    return ((l+o)*(l+v)*(l+e)*(o+v)*(o+e)*(v+e))% 100

yeonduName=input()

num=int(input())
t=0

team_win_percent={}

for i in range(num):
    teamName=input()
    t=percent_team_win(teamName,yeonduName)
    if t in team_win_percent : 
        team_win_percent[t]=min(team_win_percent[t],teamName)
        
    else : team_win_percent[t]=teamName

print(team_win_percent[max(team_win_percent)])   
