"""
완주하지 못한 선수
문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/42576
"""

def solution(participant, completion):
    answer = ''
    p_dict = {}
    for p in participant:
        p_dict.setdefault(p, 0)
        p_dict[p] += 1
    
    for c in completion:
        p_dict[c] -= 1

    for k, v in p_dict.items():
        if v > 0:
            answer = k
        
    return answer