"""
문제 이름: 신규 아이디 추천
문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/72410
"""

# 통과한 코드 (내 풀이) - 정규식 사용
import re

def solution(new_id):
    new_id = new_id.lower()
    new_id = re.sub('[^a-z0-9-_.]', '', new_id)
    new_id = re.sub('\.+', '.', new_id)
    new_id = re.sub('^\.', '', new_id)
    new_id = re.sub('\.$', '', new_id)
    if new_id == '':
        new_id = 'a'
    new_id = re.sub('\.$', '', new_id[:15])
    new_id += new_id[-1]*(3-len(new_id))
    return new_id

"""
<사용한 개념>
1. 소문자 변환
2. 정규식
  1) re.sub 문자열 치환
  2) ^문자열 == 문자열 맨 앞
  3) 문자열$ == 문자열 맨 뒤
"""