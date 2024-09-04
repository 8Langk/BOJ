def solution(survey, choices):
    mbti={'R':0,'T':0,'C':0,'F':0,'J':0,'M':0,'A':0,'N':0}

    answer=''

    for i in range(len(choices)):
        if choices[i]==1:
            mbti[survey[i][0]]=mbti[survey[i][0]]+3
        elif choices[i]==2:
            mbti[survey[i][0]]=mbti[survey[i][0]]+2
        elif choices[i]==3:
            mbti[survey[i][0]]=mbti[survey[i][0]]+1
        elif choices[i]==5:
            mbti[survey[i][1]]=mbti[survey[i][1]]+1
        elif choices[i]==6:
            mbti[survey[i][1]]=mbti[survey[i][1]]+2
        elif choices[i]==7:
            mbti[survey[i][1]]=mbti[survey[i][1]]+3


    if mbti['R']>=mbti['T']:
        answer=answer+'R'
    else:
        answer=answer+'T'
    if mbti['C']>=mbti['F']:
        answer=answer+'C'
    else:
        answer=answer+'F'
    if mbti['J']>=mbti['M']:
        answer=answer+'J'
    else:
        answer=answer+'M'
    if mbti['A']>=mbti['N']:
        answer=answer+'A'
    else:
        answer=answer+'N'
        
    return answer