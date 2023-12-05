"""
베스트 앨범
문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/42579
"""

def solution(genres, plays):
    answer = []
    genre_dict = {}
    genre_count = {}
    for i, (g, p) in enumerate(zip(genres, plays)):
        genre_dict.setdefault(g, [])
        genre_count.setdefault(g, 0)
        genre_dict[g].append((i, p))
        genre_count[g] += p

    genre_count_sorted = sorted(genre_count.items(), key=lambda x: x[1], reverse=True)
    for gc in genre_count_sorted:
        genre = gc[0]
        toptwo = [el[0] for el in sorted(genre_dict[genre], key=lambda x: x[1], reverse=True)[:2]]
        answer += toptwo
    return answer


"""
적용한 개념
1) zip, enumerate
2) dictionary 정렬 - value를 기준으로, 내림차순
3) 2차원 리스트 정렬 - 두번째 값을 기준으로
"""