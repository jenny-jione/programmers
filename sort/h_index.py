"""
문제 이름: H-Index
문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/42747
"""

def solution(citations):
    answer = 0
    citations.sort()
    for h in range(citations[-1], 0, -1):
        more_than_h = [cite for cite in citations if cite >= h]
        if len(more_than_h) >= h:
            return h
    return answer