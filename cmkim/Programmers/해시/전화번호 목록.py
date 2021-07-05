def solution(phone_book):
    answer = True
    phone_book.sort()

    # for a in range(len(phone_book)-1):
    #     len_a = len(phone_book[a])
    #     for b in range(a+1, len(phone_book)):
    #         if phone_book[a] in phone_book[b][:len_a]:
    #             answer = False

    for a in range(len(phone_book) - 1):
        len_a = len(phone_book[a])
        if phone_book[a] in phone_book[a+1][:len_a]:
            answer = False


    return answer