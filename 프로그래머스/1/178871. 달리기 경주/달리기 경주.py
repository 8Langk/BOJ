def solution(players, callings):

    rank= [i for i in range(len(players))]
    player_dict = dict(zip(players,rank))

    for i in callings:
        idx= player_dict[i]
        players[idx], players[idx-1] = players[idx-1] ,players[idx]

        player_dict[players[idx]]=idx
        player_dict[players[idx-1]]=idx-1

    
    return players