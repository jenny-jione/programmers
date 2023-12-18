"""
문제 이름: 성격 유형 검사하기
문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/118666
"""

# 통과한 코드
def solution(survey, choices):
    answer = ''
    result = {'RT': 0, 'CF': 0, 'JM': 0, 'AN': 0}
    mbti = {'RT': 'RT', 'TR': 'RT',
            'CF': 'CF', 'FC': 'CF',
            'JM': 'JM','MJ': 'JM',  
            'AN': 'AN', 'NA': 'AN' }
    rcja = {'RT': 1, 'CF': 1, 'JM': 1, 'AN': 1,
            'TR': -1, 'FC': -1, 'MJ': -1, 'NA': -1}
    for sv, c in zip(survey, choices):
        result[mbti[sv]] += rcja[sv]*(c-4)
    print(result)
    for k, v in result.items():
        if v > 0:
            answer += k[1]
        else:
            answer += k[0]
    return answer


# 개선 버전
def solution(survey, choices):
    answer = ''
    result = {'RT': 0, 'CF': 0, 'JM': 0, 'AN': 0}
    for sv, c in zip(survey, choices):
        # 정해진 순서가 아니라면
        if sv not in result.keys():
            # 뒤집으면 result의 키가 됨!
            sv = sv[::-1]
            result[sv] -= (c-4)
        else:
            result[sv] += (c-4)
    for k, v in result.items():
        if v > 0:
            answer += k[1]
        else:
            answer += k[0]
    return answer


"""
매우 비동의, 비동의, 약간 비동의, 모르겠음, 약간 동의, 동의, 매우 동의 -> 점수가 각각
3 2 1 0 1 2 3 인데
choices의 원소는
1 2 3 4 5 6 7 이므로 
4를 빼면 된다.

<새로 배운 것>
1. 문자열/리스트 뒤집기
    A = "hello"일 때 A를 뒤집으러면 아래처럼 하면 된다.
        A = A[::-1]
    리스트일 때도 동일하게 적용된다.

"""