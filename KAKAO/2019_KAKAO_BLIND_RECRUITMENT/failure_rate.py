"""
문제 이름: 실패율
문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/42889

타임라인
2024.1.3 4:23pm~4:50pm (1차)
2024.1.3 4:50pm~4:57pm (2차-성공)
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


# 한 부분 고쳤더니 성공함! 4:57pm
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
        # 스테이지에 도달한 유저가 없는 경우 해당 스테이지의 실패율은 0으로 정의한다.
        if mo == 0:
            fail_rate[i] = 0
        else:
            fail_rate[i] = ja/mo
    sorted_rate = sorted(fail_rate.items(), key=lambda x:x[1], reverse=True)
    answer = [k[0] for k in sorted_rate]
    return answer


"""
* 스테이지에 도달한 유저가 없는 경우 해당 스테이지의 실패율은 0으로 정의한다.
    if mo == 0:
        fail_rate[i] = 0
분모가 0인 부분을 처리하지 않아서 런타임에러가 발생한 것.
문제에 조건이 주어져 있었는데 놓쳤었다.
"""