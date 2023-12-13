"""
문제 이름: 같은 숫자는 싫어
문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/12906
"""

def solution(arr):
    answer = [arr[0]]
    for num in arr[1:]:
        if answer[-1] != num:
            answer.append(num)
    return answer