# ���� ������ ���� ������ ��� ������ �������� �л����� ����� �ű���� �մϴ�.
# ���� ������ ���� ������ ���� 2���� ���� �迭 score�� �־��� ��,
# ���� ������ ���� ������ ����� �������� �ű� ����� ���� �迭�� return�ϵ��� solution �Լ��� �ϼ����ּ���.

# ������ ���̽�
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
    scores = [sum(i)/len(i) for i in score] #��� ����Ʈ
    sort_scores = sorted(scores,reverse=True) #���� ���Ҷ� �̿�
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