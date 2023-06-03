# �� �� �̻��� ���� ������ �̷���� ���� ���׽��̶�� �մϴ�. ���׽��� ����� ���� �����׳��� ����� �����մϴ�.
# �������� �̷���� ���׽� polynomial�� �Ű������� �־��� ��, �����׳��� ���� �ᱣ���� ���ڿ��� return �ϵ��� solution �Լ��� �ϼ��غ�����.
# ���� ���̶�� ���� ª�� ������ return �մϴ�.

def solution(polynomial):
    answer = polynomial.split(" + ")
    a, b = 0, 0
    for i in answer:
        if i[-1] == 'x':
            a += int(i[0:-1]) if len(i) > 1 else 1
        else:
            b += int(i)
    if a == 0:
        dap = str(b)
    elif a == 1:
        if b != 0:
            dap = 'x + ' + str(b)
        elif b == 0:
            dap = 'x'
    elif a > 1:
        if b != 0:
            dap = str(a) + 'x + ' + str(b)
        elif b == 0:
            dap = str(a) + 'x'
    return dap


# def solution(polynomial):
#     xnum = 0
#     const = 0
#     for c in polynomial.split(' + '):
#         if c.isdigit():
#             const+=int(c)
#         else:
#             xnum = xnum+1 if c=='x' else xnum+int(c[:-1])
#     if xnum == 0:
#         return str(const)
#     elif xnum==1:
#         return 'x + '+str(const) if const!=0 else 'x'
#     else:
#         return f'{xnum}x + {const}' if const!=0 else f'{xnum}x'

# str(a) + 'x + ' + str(b) -- > '{}x + {}'.format(a, b) --> fstring : f'{a}x + {b}'
        

print(solution("3x + 7 + x"))