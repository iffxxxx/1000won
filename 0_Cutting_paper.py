# ���� M, N�� �Ű������� �־��� ��,
# M x N ũ���� ���̸� �ּҷ� ������ �ؾ��ϴ� Ƚ���� return �ϵ��� solution �Լ��� �ϼ��غ�����.

def solution(M, N):
    answer = M * N - 1
    return answer


# def get_cut_cnt_dfs(width, height):
#     width, height = min(width, height), max(width, height)
#     if width == 1 and height == 1:
#         return 0
#     return 1 + get_cut_cnt_dfs(width, height//2) + get_cut_cnt_dfs(width, height-height//2)

# def solution(M, N):
#     return get_cut_cnt_dfs(M, N)

# min(width, height)�� ����Ͽ� ���� ���� width, ū ���� height�� �����մϴ�. �̷��� �ϸ� �׻� width�� ���� ���� �˴ϴ�.
# ���� width�� height�� ��� 1�� ���, �� �̻� �ڸ� �ʿ䰡 �����Ƿ� 0�� ��ȯ�մϴ�.
# �׷��� ���� ���, 1 + get_cut_cnt_dfs(width, height//2) + get_cut_cnt_dfs(width, height-height//2)�� ��ȯ�մϴ�.
# ù ��° ��� ȣ���� width�� �״�� �����ϰ� height�� �������� �ڸ��� ����� �ڸ��� Ƚ���� ����մϴ�.
# �� ��° ��� ȣ���� width�� �״�� �����ϰ� height���� height//2�� �� �������� �ڸ��� ����� �ڸ��� Ƚ���� ����մϴ�.
# 1�� ������ ������ ���� �ܰ迡�� �ڸ��� Ƚ���� �����ֱ� ���ؼ��Դϴ�.

print(solution(2, 5))