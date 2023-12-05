"""
전화번호 목록
문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/42577
"""

def solution(phone_book):
    answer = True
    phone_book.sort()
    for i in range(len(phone_book)-1):
        num = phone_book[i]
        if num == phone_book[i+1][:len(num)]:
            return False
    return answer


"""
zip
startswith
사용법 !!
"""