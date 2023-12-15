"""
문제 이름: 올바른 괄호 
문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/12909
"""

def solution(s):
    bracket = 0
    for c in s:
        if c == '(':
            bracket += 1
        else:
            bracket -= 1
        if bracket < 0:
            return False
    if bracket != 0:
        return False
    return True

"""
참고)
if bracket != 0:
    return False
return True

위 코드을 아래처럼 한 줄로 줄일 수 있다.

return bracket == 0

"""