"""
문제 이름: 롤케이크 자르기
문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/132265

타임라인
2024.3.19 14:40pm~
"""

def solution(topping):
    answer = -1
    dic1 = {}
    for t in topping:
        dic1.setdefault(t, 0)
        dic1[t] += 1
    
    dic2 = {}
    for t in topping:
        dic2.setdefault(t, 0)
        dic2[t] += 1
        dic1[t] -= 1
        if dic1[t] == 0:
            del(dic1[t])
        if len(dic2) == len(dic1):
            answer += 1
    return answer