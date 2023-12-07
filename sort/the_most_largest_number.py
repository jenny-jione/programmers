"""
문제 이름: 가장 큰 수
문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/42746
"""

def solution(numbers):
    answer = ''
    zero = 0
    for n in numbers:
        zero += n
    if zero == 0:
        return "0"
    n_str = [str(n) for n in numbers]
    answer = ''.join(sorted(n_str, key=lambda x: x*3, reverse=True))
    return answer


# [0, 0] 등의 테스트케이스 처리 코드 수정
# 기존: for문으로 입력값인 numbers의 원소가 전부 0인지 확인
# 개선: int -> str 함수를 적용해서 자연스럽게 0, 00, .. 등을 -> 0 -> '0'으로 변환하여 리턴.
def solution(numbers):
    answer = ''
    n_str = [str(n) for n in numbers]
    answer = str(int(''.join(sorted(n_str, key=lambda x: x*3, reverse=True))))
    return answer

"""
TODO: functools.cmp_to_key 공부
솔직히 x*3 아이디어를 어떻게 생각해내는지..모르겠음..
이 방법 말고 functools.cmp_to_key 사용법 공부해서 그걸로 다시 구현해보기
"""