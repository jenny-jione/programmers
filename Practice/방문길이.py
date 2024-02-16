"""
문제 이름: 방문 길이
문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/49994

타임라인
2024.2.16 1:07pm~1:40pm
2024.2.16 1:45pm~2:00pm
"""

# 내가 통과한 코드
def solution(dirs):
    answer = 0
    direct = 'UDRL'
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    path = []
    x = [0, 0]
    y = [0, 0]
    for d in dirs:
        idx = direct.index(d)
        # 좌표평면의 범위 안에 있는 명령어일 경우
        if -5<= (x[0] + dx[idx]) <=5 and -5<= (y[0] + dy[idx]) <=5:
            x[1] = x[0] + dx[idx]
            y[1] = y[0] + dy[idx]
            p1 = ((x[0], y[0]), (x[1], y[1]))
            p2 = ((x[1], y[1]), (x[0], y[0]))
            path.append(p1)
            path.append(p2)
        x[0] = x[1]
        y[0] = y[1]
    answer = len(set(path))/2
    return answer


"""
< 코드 개선점 >
1. direct, dx, dy 부분을 하나로 표현할 수 있다.
2. path에 set 처리를 하는 대신 처음부터 set으로 다루자.
"""
def solution(dirs):
    s = set()
    d = {'U': (0, 1), 'D': (0, -1), 'R': (1, 0), 'L': (-1, 0)}
    x, y = 0, 0
    for i in dirs:
        nx = x + d[i][0]
        ny = y + d[i][1]
        if -5 <= nx <= 5 and -5 <= ny <= 5:
            s.add((x,y,nx,ny))
            s.add((nx,ny,x,y))
            x = nx
            y = ny
    return len(s)/2