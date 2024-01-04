"""
문제 이름: 크레인 인형뽑기 게임
문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/64061

타임라인
24.1.3 7:37pm~8:30pm
"""

def solution(board, moves):
    answer = 0
    n = len(board)
    new_board = [[] for _ in range(n)]
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


+
처음에 코드에 분명히 오류가 없는 것 같은데 계속 틀리는거다.
보니까 문제를 제대로 읽지 않아서 일어난 참사..
구해야 하는 것: 터트려져 사라진 인형의 개수
내가 구현한 것: '터진' 횟수
어쩐지.. 샘플 테스트케이스 기댓값이 4인데 나는 2가 나와서 뭘 덜 더한줄 알고 코드에 오류가 있는 줄 알았지..
"""