# ���ڿ� before�� after�� �Ű������� �־��� ��,
# before�� ������ �ٲپ� after�� ���� �� ������ 1��,
# ���� �� ������ 0�� return �ϵ��� solution �Լ��� �ϼ��غ�����.

def solution(before, after):
    return 1 if sorted(before) == sorted(after) else 0
    # return (sorted(list(before)) == sorted(list(after))) * 1
    
print(solution("lloeh","hello"))