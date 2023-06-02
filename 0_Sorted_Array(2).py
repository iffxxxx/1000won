# 영어 대소문자로 이루어진 문자열 my_string이 매개변수로 주어질 때,
# my_string을 모두 소문자로 바꾸고 알파벳 순서대로 정렬한 문자열을 return 하도록 solution 함수를 완성해보세요.

def solution(my_string):
    return ''.join(sorted([i for i in my_string.lower()]))
    # return ''.join(sorted(my_string.lower()))
    

# def solution(my_string):
#     answer = []
#     for i in my_string:
#         if ord(i) >= ord('A') and ord(i) <= ord('Z'):   # 대문자 판별 ord() == 유니코드 정수 변환
#             answer.append(chr(ord(i)+32))               # 소문자 변환
#         else:
#             answer.append(i)
#     return ''.join(sorted(answer))

