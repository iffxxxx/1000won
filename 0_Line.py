# ���� 3���� �����ϰ� ���� �ֽ��ϴ�.
# �� ������ ���۰� �� ��ǥ�� [[start, end], [start, end], [start, end]] ���·� ����ִ� 2���� �迭 lines�� �Ű������� �־��� ��,
# �� �� �̻��� ������ ��ġ�� �κ��� ���̸� return �ϵ��� solution �Լ��� �ϼ��غ�����.

def solution(lines):
    lines.sort(key = lambda x : x[0])
    a = lines[0][0]
    print(lines)
    lines.sort(key = lambda x : x[1])
    b = lines [2][1]

    line = []
    for i in range(0, b + 201):
        line.append(0)
    
    for m, n in lines:
        for j in range(m + 100, n + 100):
            line[j] += 1
    answer = line.count(2) + line.count(3)
    return answer


# def solution(lines):
#     sets = [set(range(min(l), max(l))) for l in lines]
#     return len(sets[0] & sets[1] | sets[0] & sets[2] | sets[1] & sets[2])


print(solution([[0, 5], [1, 10], [3, 9]]))