"""
문제 이름: 키패드 누르기
문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/67256
"""

"""
1 2 3
4 5 6
7 8 9
* 0 #

"""

"""
23.12.31 3:50pm~4:05pm
"""

def solution(numbers, hand):
    answer = ''
    # 무조건 L: 1, 4, 7
    # 무조건 R: 3, 6, 9
    # 현재 위치에서 가까운 손: 2, 5, 8, 0
    # 만약 거리가 같다면 주 손으로 선택.
    # 관건: 현재 위치에서 목표 위치까지의 거리 계산하기.
    # 2) 현재 위치를 업데이트 시키기.
    
    # 2~9 거리: (9-2)%3 == 1, (9-2)//3 == 2 -> 거리: 3
    # 2~8 거리: (8-2)%3 == 0, (8-2)//3 == 2 -> 거리: 2
    # 3~9 거리: (9-3)%3 == 0, (9-3)//3 == 2 -> 거리: 2
    # 따라서 거리는 나머지+몫
    
    # 키패드 0은 11로 바꾸어 계산한다.
    cur_l = 10
    cur_r = 12
    
    for n in numbers:
        if n == 0:
            n = 11
        if n in [1, 4, 7]:
            cur_l = n
            answer += 'L'
        elif n in [3, 6, 9]:
            cur_r = n
            answer += 'R'
        else:
            dl = (cur_l-n)%3 + (cur_l-n)//3
            dr = (cur_r-n)%3 + (cur_r-n)//3
            if dl < dr:
                cur_l = n
                answer += 'L'
            elif dr < dl:
                cur_r = n
                answer += 'R'
            else:
                if hand == 'left':
                    cur_l = n
                    answer += 'L'
                else:
                    cur_r = n
                    answer += 'R'
    
    return answer