"""
문제 이름: [1차]다트 게임
문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/17682
"""

import re

# 첫 풀이 - 샘플 테스트케이스 통과까지 확인
def solution(dart):
    power_dict = {'S':1, 'D':2, 'T':3}
    # 각각의 점수|보너스|[옵션]을 나누기
    grade_str = []
    for i, ch in enumerate(dart):
        if ch in 'SDT':
            if i >= 2 and dart[i-2] in '1234567890':
                d = dart[i-2:i+1]
            else:
                d = dart[i-1:i+1]
            if i < len(dart)-1 and dart[i+1] in '*#':
                d += dart[i+1]
            grade_str.append(d)

    ans = [0] * len(grade_str)
    for i, g in enumerate(grade_str):
        grade = re.split(r'(S|D|T)', g)
        grade = [s for s in grade if s]
        ans[i] = int(grade[0]) ** power_dict[grade[1]]
        if grade[-1] == '*':
            if i > 0:
                ans[i-1] *= 2
            ans[i] *= 2
        elif grade[-1] == '#':
            ans[i] *= -1
    answer = sum(ans)
    return answer


# re.compile을 적용한 풀이 - ing
def solution(dart_result):
    power_dict = {'S':1, 'D':2, 'T':3}
    # p = re.compile('(\d{1,2})([SDT])([*#]?)')
    p = re.compile('\d{1,2}[SDT][*#]?')
    dart = p.findall(dart_result)
    print(dart)
    

"""
re.compile

1.  p = re.compile('(\d{1,2})([SDT])([*#]?)')
    dart = p.findall(dart_result)
        각 괄호 안에 있는 것들이 하나의 개별 원소로 들어감.
        예) "1S2D*3T" => [('1', 'S', ''), ('2', 'D', '*'), ('3', 'T', '')]

2.  p = re.compile('\d{1,2}[SDT][*#]?')
    dart = p.findall(dart_result)
        해당 패턴에 맞는 것이 통째로 들어감.
        예) "1S2D*3T" => ['1S', '2D*', '3T']
"""