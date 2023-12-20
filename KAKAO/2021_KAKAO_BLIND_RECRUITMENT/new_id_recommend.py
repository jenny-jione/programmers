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


# 정규식 사용하지 않고 풀어보기
def solution(new_id):
    # 1.소문자 치환
    new_id = new_id.lower()
    
    # 2.알파벳 소문자, 숫자, -, _, .를 제외한 모든 문자 제거
    answer = ''
    for ch in new_id:
        if ch in '1234567890abcdefghijklmnopqrstuvwxyz-_.':
            answer += ch

    # # 3.마침표가 연속된 부분을 하나의 마침표로 치환
    while '..' in answer:
        answer = answer.replace('..', '.')
    
    # 4.마침표가 처음이나 끝에 위치한다면 제거
    if answer[0] == '.':
        answer = answer[1:] if len(answer) > 1 else '.'
    
    if answer[-1] == '.':
        answer = answer[:-1]
    
    # 5.빈 문자열일 경우 a 대입
    if answer == '':
        answer = 'a'
    
    # 6.길이가 16자 이상일 경우 앞 15자만 취하기 & 마침표가 끝이라면 마침표 제거
    answer = answer[:15]
    if answer[-1] == '.':
        answer = answer[:-1]
    
    # 7.길이가 2자 이하라면 길이가 3이 될 때까지 마지막 문자를 이어붙이기
    answer += answer[-1] * (3-len(answer))
        
    return answer


"""
<사용한 개념>
1. 소문자 변환
2. 정규식
  1) re.sub 문자열 치환
  2) ^문자열 == 문자열 맨 앞
  3) 문자열$ == 문자열 맨 뒤
"""