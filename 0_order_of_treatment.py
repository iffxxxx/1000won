# �ܰ��ǻ� �Ӿ��̴� ���޽ǿ� �� ȯ���� ���޵��� �������� ���� ������ ���Ϸ��� �մϴ�.
# ���� �迭 emergency�� �Ű������� �־��� �� ���޵��� ���� ������� ���� ������ ���� �迭�� return�ϵ��� solution �Լ��� �ϼ����ּ���.

def solution(emergency):
    answer = []
    tmp = sorted(emergency, reverse = True)
    for i in emergency:
        answer.append(tmp.index(i)+1)
    return answer


# def solution(emergency):
#     arr = []
#     for i in emergency:
#         idx = 1
#         for j in emergency:
#             if i < j:
#                 idx += 1
#         arr.append(idx)
#     return arr

print(solution([3, 76, 24]))