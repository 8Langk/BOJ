def solution(phone_book):
    answer = True    
    phone_book.sort()
    
    for i in range(0,len(phone_book)-1):
        if phone_book[i] == phone_book[i+1][:len(phone_book[i])]:
            return False
            break
            
    '''book = {i : 1 for i in phone_book}
    
    book = dict(sorted(book.items(), key= lambda x : len(x[0])))
    
    for i in book:
        temp=""
        for 엄준식 in i:
            temp+=엄준식
            if temp in book and temp!=i:
                return False '''     
    return answer