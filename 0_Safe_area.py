def solution(board):
    offset = [[-1, 1], [-1, 0], [-1, -1], [0, 1], [0, -1], [1, 1], [1, 0], [1, -1]]
    for i in range(len(board[0])):
        for j in range((len(board))):
            if board[i][j] == 1:
                for m in offset:
                    x = i + m[0]
                    y = j + m[1]
                    if x >= 0 and x < len(board[0]) and y >= 0 and y < len(board):
                        if board[x][y] == 0:
                            board[x][y] = 2
    count = 0
    for c1 in board:
        for c2 in c1:
            if c2 == 0:
                count += 1
    return count


# def solution(board):
#     n = len(board)
#     danger = set()
#     for i, row in enumerate(board):
#         for j, x in enumerate(row):
#             if not x:                 # 0 = True 1 = False
#                 continue
#             danger.update((i+di, j+dj) for di in [-1,0,1] for dj in [-1, 0, 1])
#     return n*n - sum(0 <= i < n and 0 <= j < n for i, j in danger)

print(solution([[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 1, 0, 0], [0, 0, 0, 0, 0]]))