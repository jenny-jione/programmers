"""
문제 이름: 모의고사
문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/42840
"""

def solution(answers):
    answer = []
    supo = [0, 0, 0]
    for i, ans in enumerate(answers):
        ans = str(ans)
        if "12345"[i%5] == ans:
            supo[0] += 1
        if "21232425"[i%8] == ans:
            supo[1] += 1
        if "3311224455"[i%10] == ans:
            supo[2] += 1
    best = max(supo)
    answer = [(i+1) for i, grade in enumerate(supo) if grade==best]
    return answer

"""
각각 주기가 5, 8, 10인데, 이걸 나는 문자열로 선언했기 때문에 반복문마다 ans를 문자열로 바꾸어서 비교하는 과정이 필요.
(처음에 "12345"[i%5]와 ans를 단순 비교했다가, 문자열과 정수를 비교하게 되어서 틀렸었음)

다른 사람의 풀이를 보니까, "12345", "21232425", "3311224455"를 숫자 리스트 변수로 선언한 후에, 리스트의 인덱스와 답을 비교하게 코드를 짬.
내 코드의 단점: 만약 패턴이 바뀐다면, 나는 주기를 그냥 숫자로 넣어두었기 때문에 코드 수정이 필요. ([i%5], [i%8], [i%10] 이 부분)
"""