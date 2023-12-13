"""
문제 이름: 기능개발
문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/42586
"""

import math

def solution(progresses, speeds):
    answer = []
    while(progresses):
        # 제일 먼저 배포되어야 하는 기능의 남은 날짜 계산. 만약 개발율이 95%이고 speed가 4라면 2일 뒤에 배포되므로 나눈 값을 올림해야 함.
        day = math.ceil((100-progresses[0])/speeds[0])

        # zip을 사용하여 progresses[0]이 100일 때의 나머지 기능들의 개발율 재계산
        baepo = [p+day*s for p, s in zip(progresses, speeds)]
        progresses = []
        for i, b in enumerate(baepo):
            # 만약 100이 되지 않은 기능이 있다면 그 이후의 기능들도 모두 배포가 불가능하므로 반복문 종료.
            if b < 100:
                answer.append(i)
                progresses = baepo[i:]
                speeds = speeds[i:]
                break
    if len(baepo) > 0:
        answer.append(len(baepo))
    return answer


"""
사용한 개념
1. math.ceil
2. zip - 2개의 리스트를 for문을 돌릴 때 사용
"""