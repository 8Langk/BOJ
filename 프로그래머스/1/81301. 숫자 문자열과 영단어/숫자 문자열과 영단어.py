def solution(s):
    dic={"zero":"0","one":"1", "two":"2", "three":"3", "four":"4", "five":"5", "six":"6", "seven":"7", "eight":"8", "nine":"9"}

    length = len(s)
    neww = ''
    answer=''

    for i in range(length):
        if ord(s[i])>=48 and ord(s[i])<=57:
            answer+=s[i]
        else :
            neww+=s[i]

            if neww in dic :
                answer += dic[neww]
                neww=''

    return int(answer)