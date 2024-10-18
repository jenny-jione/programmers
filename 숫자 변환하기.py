"""
문제 이름: 숫자 변환하기
문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/154538
문제 티어: Lv.2

타임라인
2024.10.18 04:15pm~04:34pm (19분)  total: 19분

<정리>
1. BFS
2. for nx in (x + n, x * 2, x * 3) 으로 코드를 간결하게 바꿀 수 있다.
"""

from collections import deque

def solution(x, y, n):
    dist = [-1] * (y+1)
    q = deque([x])
    dist[x] = 0
    while q:
        x = q.popleft()
        if x == y:
            return dist[x]
        nx = x + n
        if nx <= y and dist[nx]==-1:
            dist[nx] = dist[x] + 1
            q.append(nx)
        nx = x * 2
        if nx <= y and dist[nx]==-1:
            dist[nx] = dist[x] + 1
            q.append(nx)
        nx = x * 3
        if nx <= y and dist[nx]==-1:
            dist[nx] = dist[x] + 1
            q.append(nx)
    return -1


# 개선된 코드
from collections import deque

def solution(x, y, n):
    dist = [-1] * (y+1)
    q = deque([x])
    dist[x] = 0
    while q:
        x = q.popleft()
        if x == y:
            return dist[x]
        for nx in (x+n, x*2, x*3):
            if nx <= y and dist[nx]==-1:
                dist[nx] = dist[x] + 1
                q.append(nx)
    return -1