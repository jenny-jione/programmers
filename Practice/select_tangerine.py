"""
문제 이름: 귤 고르기
문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/138476

타임라인
2024.2.15 12:20pm ~ 12:28pm
"""

# 통과한 코드
def solution(k, tangerine):
    answer = 0
    # 개수가 많은 것부터 세면 종류가 적어짐.
    kind = {}
    for t in tangerine:
        kind.setdefault(t, 0)
        kind[t] += 1
    
    sorted_kind = sorted(kind.items(), key = lambda x: x[1], reverse = True)
    
    for key, val in sorted_kind:
        k -= val
        answer += 1
        if k <= 0:
            break
    return answer


"""
코드 개선.
정렬 과정과 그 이후도 key는 필요없음.
sorted가 간결해진다.
sorted(kind.values(), reverse = True)
"""

def solution(k, tangerine):
    answer = 0
    # 개수가 많은 것부터 세면 종류가 적어짐.
    kind = {}
    for t in tangerine:
        kind.setdefault(t, 0)
        kind[t] += 1
    
    sorted_kind = sorted(kind.values(), reverse = True)
    
    for val in sorted_kind:
        k -= val
        answer += 1
        if k <= 0:
            break
    return answer