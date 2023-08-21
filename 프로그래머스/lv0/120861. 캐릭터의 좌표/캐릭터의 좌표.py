def solution(keyinput, board):
    answer = []
    #up, down, rignt, left 순서
    dir_x = [0, 0, 1, -1]
    dir_y = [1, -1, 0, 0]
    dir_n = ["up", "down", "right", "left"]

    x , y = 0,0
    max_x, min_x = board[0] // 2, -(board[0] // 2)
    max_y, min_y = board[1] // 2, -(board[1] // 2)

#     for i in range(len(keyinput)):
        
#         if keyinput[i] in dir_n:
            
#             if abs(x) < board[0] // 2:
#                 x += dir_x[dir_n.index(keyinput[i])]
#             else:
#                 if x <= 0:
#                     x = min_x
#                 else:
#                     x = max_x
                
#             if abs(y) < board[1] // 2:
#                 y += dir_y[dir_n.index(keyinput[i])]
#             else:
#                 if y <= 0:
#                     y = min_y
#                 else:
#                     y = max_y
    for i in range(len(keyinput)):
        
        if keyinput[i] in dir_n:
            x += dir_x[dir_n.index(keyinput[i])]
            y += dir_y[dir_n.index(keyinput[i])]

            if x < min_x or x > max_x: #범위를 벗어나면
                x = x- dir_x[dir_n.index(keyinput[i])] #직전에 한거 취소
            if y < min_y or y > max_y: #범위를 벗어나면
                y = y- dir_y[dir_n.index(keyinput[i])] #직전에 한거 취소

                    
    answer.append(x)
    answer.append(y)

    return answer