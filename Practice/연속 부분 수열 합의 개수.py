"""
문제 이름: 연속 부분 수열 합의 개수
문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/131701

타임라인
2024.2.15 2:46pm~3:07pm (21분)
"""


# 2024.2.15 2:46pm~

def solution(elements):
    answer = 0
    result = []
    n = len(elements)
    # 길이별로
    for length in range(1, n):
        for start in range(n):
            # end 인덱스를 n보다 크게 나오지 않도록 나눠주기.
            end = (start + length) % n

            # [2:1]같은 경우 이대로 인덱싱을 하면 빈 리스트가 나온다.
            # 그래서 [2:] + [:1] 로 쪼개주는 역할.
            if end < start:
                hap = sum(elements[start:]) + sum(elements[:end])

            # 일반적인 경우. [1:3]
            else:
                hap = sum(elements[start:end])
            result.append(hap)
    # 길이가 n인 연속 부분 수열 합
    result.append(sum(elements))
    answer = len(set(result))
    return answer


"""
1. range(1, n)
1부터 n-1까지가 나온다. 
"""