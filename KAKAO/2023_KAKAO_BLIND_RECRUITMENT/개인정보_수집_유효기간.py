"""
문제 이름: 개인정보 수집 유효기간
문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/150370
"""

def solution(today, terms, privacies):
    answer = []
    removal = {}
    # {약관종류: 유효기간} dictionary 생성
    for term in terms:
        kind, month = term.split()
        removal[kind] = int(month)
    
    # 각 개인정보마다
    for idx, privacy in enumerate(privacies):
        collect_date, kind = privacy.split()
        y, m, d = [int(date_split) for date_split in collect_date.split('.')]

        # 약관 종류로 검색 후
        term_m = removal[kind]
        month_sum = m + term_m
        destroy_y = y + (month_sum-1)//12
        destroy_m = month_sum%12
        destroy_d = d
        if destroy_m == 0:
            destroy_m = 12
        destroy_date = str(destroy_y) + '.' + str(destroy_m).zfill(2) + '.' + str(destroy_d).zfill(2)

        # 넘었는지 안넘었는지 확인하기 - 넘었으면 파기. answer에 담기
        if today >= destroy_date:
            answer.append(idx+1)
    return answer


"""
<새로 배운 것>
1. list comprehension는 dictionary에도 사용할 수 있다.
2. map 사용법
    나의 코드 중에
        y, m, d = [int(date_split) for date_split in collect_date.split('.')]
    위 부분을 아래처럼 더 간소화할 수 있다.
        y, m, d = map(int, collect_date.split('.'))
"""