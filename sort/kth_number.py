"""
문제 이름: K번째수
문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/42748
"""

def solution(array, commands):
    answer = []
    for c in commands:
        i = c[0]-1
        j = c[1]
        k = c[2]-1
        answer.append(sorted(array[i:j])[k])
    return answer

"""
개선 가능한 부분
i, j, k를 한번에 입력(선언)할 수 있다.
    i, j, k = command

또는 for문 자체에서도 선언 가능하다.
    for i, j, k in commands:

단, 위처럼 선언할 경우 정렬하는 array의 인덱스 설정이 아래처럼 바뀌어야 한다.
    answer.append(sorted(array[i-1:j])[k-1])
"""