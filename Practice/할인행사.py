"""
문제 이름: 할인 행사
문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/131127

타임라인
2024.2.16 11:39am~11:51am (12분)
"""

def solution(want, number, discount):
    answer = 0
    want_dict = {w:n for w, n in zip(want, number)}
    discountday = len(discount)
    for i in range(discountday-10+1):
        buy = discount[i:i+10]
        check = True
        for k, v in want_dict.items():
            if v != buy.count(k):
                check = False
                break
        if check:
            answer += 1
    return answer


"""
사용한 개념
1. 딕셔너리 컴프리헨션
    want와 number가 각각의 개별 리스트인데 관계를 지어주기 위해서 딕셔너리 컴프리헨션과 zip을 사용했다.
2. 리스트의 count() 함수 사용
    discount 리스트의 부분 리스트(길이 10짜리)가 문제의 주어진 조건을 만족하는지의 여부를 판단하기 위해서 사용했다.
    *개선 방향: from collections import Counter 사용해보기.
"""