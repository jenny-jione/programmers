"""
문제 이름: 파일명 정렬
문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/17686

타임라인
2024.1.29 3:20pm~3:50pm
"""

import re

def solution(files):
    temp = [re.split(r'([0-9]+)', file) for file in files]
    new_files = [[file[0].lower(), int(file[1]), ''.join(file)] for file in temp]
    sorted_files = sorted(new_files, key=lambda x: (x[0], x[1]))
    answer = [sf[-1] for sf in sorted_files]
    return answer


"""
re의 split
re.split(r'(정규표현식)', 문자열) 일 경우, 구분자로 사용된 정규표현식도 포함해서 저장한다.
대소문자는 정렬 순서에 영향을 주지 말아야 하므로 모두 소문자로 바꾼 값을 기준으로 정렬.
숫자 부분은 문자열이 아니라 숫자 취급해야 하므로 int로 변환.

기억할 것
1. re 활용 방법 - 여기서는 split을 썼지만, findall, match, search 사용 방법도 익혀두기
2. sorted(원래 데이터, 키로 정렬기준 주기)
    sorted(new_files, key=lambda x: (x[0], x[1]))
"""