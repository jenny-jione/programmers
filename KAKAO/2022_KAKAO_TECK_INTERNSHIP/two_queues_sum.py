"""
문제 이름: 두 큐 합 같게 만들기
문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/118667

타임라인
2024.1.29 1:40pm~2:45pm
"""

# 시간초과 코드. (11,12,15,19~등 그리고 29)
from collections import deque

def pop_and_insert(q_from: deque, q_to: deque):
    q_to.append(q_from.popleft())

def solution(queue1, queue2):
    answer = 0
    q1 = deque(queue1)
    q2 = deque(queue2)

    qsum = sum(q1) + sum(q2)
    if qsum % 2 == 1:
        return -1
    qmax = max(max(q1), max(q2))
    if qmax*2 > qsum:
        return -1
    
    while(sum(q1)!=sum(q2)):
        if sum(q1) < sum(q2):
            pop_and_insert(q2, q1)
            answer += 1
        elif sum(q1) > sum(q2):
            pop_and_insert(q1, q2)
            answer += 1
    
    return answer


# 수정해서 통과한 코드
from collections import deque

def solution(queue1, queue2):
    answer = 0
    n = len(queue1)
    q1 = deque(queue1)
    q2 = deque(queue2)
    s1 = sum(q1)
    s2 = sum(q2)

    if (s1+s2) % 2 == 1:
        return -1
    
    while(s1!=s2):
        if s1 < s2:
            element = q2.popleft()
            q1.append(element)
            s1 += element
            s2 -= element
            answer += 1
        elif s1 > s2:
            element = q1.popleft()
            q2.append(element)
            s1 -= element
            s2 += element
            answer += 1
        if answer == 3*n:
            return -1
    
    return answer


"""
반복문마다 sum 함수를 사용한 것이 시간 초과의 원인이었다.
while 문 내의 sum(q1), sum(q2) 부분을 없애고 while문 들어가기 전에 s1, s2를 설정해서 합에서 덧셈뺄셈을 해주었더니 해결.
"""