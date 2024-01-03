"""
문제 이름: [1차]비밀지도
문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/17681

타임라인
24.1.3 9:31am~9:55am
"""

def get_binary(deci, n):
    if deci == 0:
        return n * '0'
    bi = ''
    while deci > 1:
        bi = str(deci%2) + bi
        deci = deci//2
    bi = '1' + bi
    return (n-len(bi))*'0' + bi

def solution(n, arr1, arr2):
    answer = []
    for x1, x2 in zip(arr1, arr2):
        b1 = get_binary(x1, n)
        b2 = get_binary(x2, n)
        tmp = ''
        for e1, e2 in zip(b1, b2):
            if e1=='0' and e2=='0':
                tmp += ' '
            else:
                tmp += '#'
        answer.append(tmp)
    return answer