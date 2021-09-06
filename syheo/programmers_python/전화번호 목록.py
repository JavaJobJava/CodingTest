#프로그래머스 
#고득점 Kit
#해시
#level2
#전화번호 목록

#아이디어 
#phone_book을 set형으로 하나 저장하고
#모든 전화번호의 0~len(전화번호) 문자열이 phone_book_set에 있는지 탐색 

def solution(phone_book):
    answer = True
    phone_book_set = set(phone_book)
    for i in range(len(phone_book)):
        for j in range(1,len(phone_book[i])):
            if phone_book[i][:j] in phone_book_set:
                return False 
    return answer