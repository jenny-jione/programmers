"""
문제 이름: 주식가격
문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/42584
"""

# 효율성 테스트 통과 x
def solution(prices):
    answer = []
    for i, pi in enumerate(prices):
        up = 0
        for j, pj in enumerate(prices[i+1:]):
            if pi <= pj:
                up += 1
            else:
                up += 1
                break
        answer.append(up)
    return answer