"""
문제 이름: 뒤에 있는 큰 수 찾기
문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/154539
문제 티어: Lv.2

타임라인
2024.10.18 05:19pm~05:25pm (6분)  total: 6분

<정리>
1. 스택
2. enumerate를 잘 활용하자
3. 배열의 인덱스를 저장하면, 배열값을 저장할 필요는 없다. (중복됨)
"""

# 내 코드
def solution(numbers):
    answer = [-1] * len(numbers)
    s = [(0, numbers[0])]
    for i in range(1, len(numbers)):
        if s:
            while s and s[-1][1] < numbers[i]:
                idx, num = s.pop()
                answer[idx] = numbers[i]
        s.append((i, numbers[i]))            
    return answer


# 개선 1. 불필요한 부분 제거
def solution(numbers):
    answer = [-1] * len(numbers)
    s = []
    for i in range(len(numbers)):
        while s and numbers[s[-1]] < numbers[i]:
            answer[s.pop()] = numbers[i]
        s.append(i)            
    return answer


# 개선 2. enumerate 사용
def solution(numbers):
    answer = [-1] * len(numbers)
    stack = []
    for i, num in enumerate(numbers):
        while stack and numbers[stack[-1]] < num:
            answer[stack.pop()] = num
        stack.append(i)            
    return answer