"""
문제 이름: 최소직사각형
문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/86491
"""

def solution(sizes):
    for card in sizes:
        card.sort()
    max_w = max([card[0] for card in sizes])
    max_h = max([card[1] for card in sizes])
    return max_w * max_h