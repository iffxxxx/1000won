# �Ӿ��̴� RPG������ �ϰ� �ֽ��ϴ�. ���ӿ��� up, down, left, right ����Ű�� ������ �� Ű�� ������ ��, �Ʒ�, ����, ���������� �� ĭ�� �̵��մϴ�.
# ���� ��� [0,0]���� up�� �����ٸ� ĳ������ ��ǥ�� [0, 1], down�� �����ٸ� [0, -1], left�� �����ٸ� [-1, 0], right�� �����ٸ� [1, 0]�Դϴ�.
# �Ӿ��̰� �Է��� ����Ű�� �迭 keyinput�� ���� ũ�� board�� �Ű������� �־����ϴ�.
# ĳ���ʹ� �׻� [0,0]���� ������ �� Ű �Է��� ��� ���� �ڿ� ĳ������ ��ǥ [x, y]�� return�ϵ��� solution �Լ��� �ϼ����ּ���.

# [0, 0]�� board�� �� �߾ӿ� ��ġ�մϴ�.
# ���� ��� board�� ���� ũ�Ⱑ 9��� ĳ���ʹ� �������� �ִ� [-4, 0]���� ���������� �ִ� [4, 0]���� �̵��� �� �ֽ��ϴ�.

# def solution(keyinput, board):
#     keydict = {"left" : [-1,0], "right" : [1,0], "up" : [0,1], "down" : [0,-1]}
#     answer = [keydict[i] for i in keyinput]
#     return [answer[i][0] for i in range(len(answer))]

def solution(keyinput, board):
    answer = [0, 0]
    for i in keyinput:
        if i == "left":
            # answer[0] = max(answer[0] - 1, -(answer[0] // 2))
            if answer[0] != -(board[0] // 2):
                answer[0] -= 1
        if i == "right":
            if answer[0] != (board[0] // 2):
                answer[0] += 1
        if i == "down":
            if answer[1] != -(board[1] // 2):
                answer[1] -= 1
        if i == "up":
            if answer[1] != (board[1] // 2):
                answer[1] += 1
    return answer


# def solution(keyinput, board):
#     x_lim,y_lim = board[0]//2,board[1]//2
#     move = {'left':(-1,0),'right':(1,0),'up':(0,1),'down':(0,-1)}
#     x,y = 0,0
#     for k in keyinput:
#         dx,dy = move[k]
#         if abs(x+dx)>x_lim or abs(y+dy)>y_lim:
#             continue
#         else:
#             x,y = x+dx,y+dy
#     return [x,y]

print(solution(["left", "right", "up", "right", "right"],[11, 11]))