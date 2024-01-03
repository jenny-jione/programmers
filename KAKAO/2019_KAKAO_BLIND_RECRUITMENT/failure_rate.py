"""
문제 이름: 실패율
문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/42889

타임라인
2024.1.3 4:23pm~4:50pm (1차)
"""

# 채점결과 - 정확성: 70.4 (런타임에러:1,6,7,9,13,23,24,25)
def solution(N, stages):
    fail_rate = {i:0 for i in range(1, N+1)}
    for i in range(1, N+1):
        mo = 0
        ja = 0
        for stage in stages:
            if i <= stage:
                mo += 1
            if i == stage:
                ja += 1
        fail_rate[i] = ja/mo
    sorted_rate = sorted(fail_rate.items(), key=lambda x:x[1], reverse=True)
    answer = [k[0] for k in sorted_rate]
    return answer

