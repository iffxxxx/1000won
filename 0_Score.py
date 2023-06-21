# 영어 점수와 수학 점수의 평균 점수를 기준으로 학생들의 등수를 매기려고 합니다.
# 영어 점수와 수학 점수를 담은 2차원 정수 배열 score가 주어질 때,
# 영어 점수와 수학 점수의 평균을 기준으로 매긴 등수를 담은 배열을 return하도록 solution 함수를 완성해주세요.

# 실패한 케이스
# def solution(score):
#     sco_ind = sorted(score, key = lambda x : x[0] + x[1], reverse= True)
#     answer = score
#     sumans = [sum(i) for i in answer]
#     print(sumans.index(150))
#     for m, n in enumerate(sco_ind):
#         if sumans.count(sum(n)) == 1:
#             answer[score.index(n)] = m + 1
#         else:
#             answer[score.index(n)] = m + sumans[m:].count(sum(n))
#     return answer


def solution(score):
    answer = []
    sort_scores = []
    scores = [sum(i)/len(i) for i in score] #평균 리스트
    sort_scores = sorted(scores,reverse=True) #순위 구할때 이용
    for i in scores:
        answer.append(sort_scores.index(i)+1)
    return answer


# def solution(score):
#     rank = sorted([sum(s) / 2 for s in score], reverse=True)
#     rankDict = {}
#     for i, r in enumerate(rank):
#         if r not in rankDict.keys():
#             rankDict[r] = i + 1
#             print(i, rankDict)
#     return [rankDict[sum(s) / 2] for s in score]


print(solution([[80, 70], [70, 80], [30, 50], [90, 100], [100, 90], [100, 100], [10, 30]]))
# 150, 150, 80, 190, 190, 200, 40