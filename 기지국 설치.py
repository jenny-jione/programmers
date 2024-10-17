"""
문제 이름: 기지국 설치
문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/12979
문제 티어: Lv.

타임라인
2024.10.17 11:05pm~11:51pm (46분)
2024.10.17 08:20am~09:14am (54분)  total: 100분

<정리>
1. 그리디 알고리즘: 매 단계에서 최선의 선택을 하면서 문제를 해결
2. 구간 커버링: 연속된 구간을 최소한의 자원으로 덮는 문제
"""

# 내 코드
def build(empt, w):
    cnt = empt // (w*2+1)
    if empt % (w*2+1) != 0:
        return cnt + 1
    return cnt

def solution(n, stations, w):
    answer = 0
    # 첫번째 빈 구간
    a = 1
    b = stations[0] - w - 1
    if a <= b:
        empt = b-a+1
        answer += build(empt, w)
    
    # 중간 빈 구간
    for i in range(len(stations)-1):
        a = stations[i]+w+1
        b = stations[i+1]-w-1
        if a <= b:
            empt = b-a+1
            answer += build(empt, w)
    # 마지막 빈 구간
    a = stations[-1]+w+1
    b = n
    if a<=b:
        empt = b-a+1
        answer += build(empt, w)
        
    return answer


# 개선 코드
def solution(n, stations, w):
    answer = 0
    cur = 1
    for station in stations:
        cover_start = station - w
        if cur < cover_start:
            empty_len = cover_start - cur
            print((empty_len + 2*w)//(2*w+1))
            answer += (empty_len + 2*w)//(2*w+1)
        cur = station + w + 1
        
    if cur <= n:
        empty_len = n - cur + 1
        answer += (empty_len + 2*w)//(2*w+1)
    return answer