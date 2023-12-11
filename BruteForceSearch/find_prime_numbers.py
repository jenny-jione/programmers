"""
문제 이름: 소수 찾기
문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/42839
"""

import itertools

def is_prime(n):
    if n < 2:
        return False
    elif n == 2:
        return True
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

def solution(numbers):
    answer = 0
    num_list = []
    for r in range(1, len(numbers)+1):
        nPr = list(itertools.permutations(numbers, r))
        for num in nPr:
            per_num = int(''.join(list(num)))
            num_list.append(per_num)
    num_set = list(set(num_list))
    for n in num_set:
        if is_prime(n):
            answer += 1
    return answer


"""
itertools.permutations 새로 알게 됨
** 연산자 - 거듭제곱
"""