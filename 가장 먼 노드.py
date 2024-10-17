"""
문제 이름: 가장 먼 노드
문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/49189
문제 티어: Lv.3

타임라인
2024.10.17 04:43pm~04:57pm (14분)
2024.10.17 06:19pm~06:38pm (19분)  total: 33분

<정리>
1. 그래프 탐색
2. BFS
3. 최단 경로
"""

# 제출해서 통과한 코드
from collections import deque

def bfs(graph, distance, start, target):
    q = deque([start])
    visited = [0] * len(graph)
    visited[start] = 1
    distance[start] = 0
    while True:
        v = q.popleft()
        if v == target:
            break
        for nv in graph[v]:
            if visited[nv]==0:
                visited[nv] = 1
                distance[nv] = distance[v] + 1
                q.append(nv)
    
def solution(n, edge):
    graph = [[] for _ in range(n+1)]
    for u, v in edge:
        graph[u].append(v)
        graph[v].append(u)
    
    for i in range(1, n+1):
        graph[i].sort()
    
    distance = [-1] * (n+1)
    for i in range(1, n+1):
        if distance[i] == -1:
            bfs(graph, distance, 1, i) 
    return distance.count(max(distance))


# 불필요한 부분 제거하고 개선
from collections import deque

def bfs(graph, distance, start):
    q = deque([start])
    distance[start] = 0
    while q:
        v = q.popleft()
        for nv in graph[v]:
            if distance[nv] == -1:
                distance[nv] = distance[v] + 1
                q.append(nv)
    
def solution(n, edge):
    graph = [[] for _ in range(n+1)]
    for u, v in edge:
        graph[u].append(v)
        graph[v].append(u)
    
    for i in range(1, n+1):
        graph[i].sort()
    
    distance = [-1] * (n+1)
    bfs(graph, distance, 1) 
    return distance.count(max(distance))