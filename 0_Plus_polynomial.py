# 한 개 이상의 항의 합으로 이루어진 식을 다항식이라고 합니다. 다항식을 계산할 때는 동류항끼리 계산해 정리합니다.
# 덧셈으로 이루어진 다항식 polynomial이 매개변수로 주어질 때, 동류항끼리 더한 결괏값을 문자열로 return 하도록 solution 함수를 완성해보세요.
# 같은 식이라면 가장 짧은 수식을 return 합니다.

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