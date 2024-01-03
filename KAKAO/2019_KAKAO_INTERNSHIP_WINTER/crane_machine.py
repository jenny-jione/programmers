"""
문제 이름: 크레인 인형뽑기 게임
문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/64061

타임라인
24.1.3 7:37pm~8:30pm
"""

def solution(board, moves):
    answer = 0
    n = len(board)
    new_board = [[] for i in range(n)]
    basket = []
    for i in range(n):
        for j in range(n):
            if board[j][i] != 0:
                new_board[i].insert(0, board[j][i])
    
    for move in moves:
        if new_board[move-1]:
            pick = new_board[move-1].pop()
            if not basket:
                basket.append(pick)
            else:
                if basket[-1] == pick:
                    basket.pop()
                    answer += 2
                else:
                    basket.append(pick)
    return answer

"""
< 사용한 개념 & 정리 >
1. list의 insert
2. list를 스택처럼 사용하기
    1) list.pop()을 하면 리스트의 마지막값이 반환되고 삭제된다.
3. 빈 리스트를 pop하려고 하면 에러가 발생한다.
4. 빈 리스트에 인덱스로 접근하면 에러가 발생한다. 
"""