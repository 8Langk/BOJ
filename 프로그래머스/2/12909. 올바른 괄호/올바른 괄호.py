def solution(s):
    answer = True
    st =[]
    '''for i in range(len(s)//2):
        if '()' in s :
            s= s.replace('()','')
            if (len(s)):
                continue
            else :
                return True
    return False
    '''

    index = 0
    i=0
    
    while i<len(s):
        st.append(s[i])
        if st[0] == ')':
            return False
        if index >=1:
            if st[index-1] == '(' and st[index] == ')':
                st.pop()
                index-=1
                st.pop()
                index-=1
        index+=1
        i+=1

    if len(st):
        return False
    else :
        return True
