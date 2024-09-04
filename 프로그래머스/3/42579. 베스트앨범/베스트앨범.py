def solution(genres, playes):
    answer = []
    genre_count = {}
    genre_play_lists={}

    for i in range(len(genres)):
        if genres[i] not in genre_count:
            genre_count[genres[i]]=playes[i]
        else : 
            genre_count[genres[i]]+=playes[i]
            
    genre_count = dict(sorted(genre_count.items(), key= lambda x : -x[1]))
    
    for i, genre in enumerate(genres):
        if genre in genre_play_lists:
            genre_play_lists[genre].append((i,playes[i]))
        else:
            genre_play_lists[genre] = [(i,playes[i])]

    for i in genre_play_lists:
        genre_play_lists[i].sort(key= lambda x :(-x[1],x[0]))
        genre_play_lists[i]=genre_play_lists[i][:2]
       

    for i in genre_count:
        if i in genre_play_lists:
            for item in genre_play_lists[i]:
                answer.append(item[0])

    return answer