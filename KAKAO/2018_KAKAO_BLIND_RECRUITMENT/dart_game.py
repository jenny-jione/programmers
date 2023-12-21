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


"""
re.compile 공부하기 => 정리해서 글 올리기
"""