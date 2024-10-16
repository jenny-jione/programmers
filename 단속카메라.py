"""
문제 이름: 단속카메라
문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/42884
문제 티어: Lv.3

타임라인
2024.10.16 02:16pm~02:25pm (9분)
2024.10.16 02:45pm~03:30pm (45분)
2024.10.16 03:54pm~04:20pm (26분)  total: 80분

<정리>
1. 그리디 알고리즘
2. sort(key=lambda x:x[1])
"""

# 내 코드
def solution(routes):
    answer = 0
    routes.sort(key=lambda x:x[1])
    n = len(routes)
    car = [0] * n
    for i in range(n):
        if car[i] == 1:
            continue
        endpoint = routes[i][1]
        cam = False
        for j in range(n):
            if routes[j][0] <= endpoint <= routes[j][1]:
                car[j] = 1
                cam = True
        if cam:
            answer += 1
    return answer


# 개선된 코드
def solution(routes):
    routes.sort(key=lambda x: x[1])  # 나가는 지점을 기준으로 정렬
    answer = 0
    last_camera = -30001  # 카메라 설치 지점을 추적 (-30001은 경로의 최소값보다 작게 설정)

    for route in routes:
        # 현재 차량이 마지막 카메라로 커버되지 않으면 새 카메라 설치
        if last_camera < route[0]:
            answer += 1
            last_camera = route[1]  # 카메라를 현재 차량의 나가는 지점에 설치
    
    return answer