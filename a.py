
def minimax(board, depth, isMaximizing):
    if isWin(board, comp) == True:
        return 1
    elif isWin(board, player) == True:
        return -1
    elif fullBoard() == True:
        return 0

    if isMaximizing == True:
        bestScore = -10000
        for i in range(3):
            for j in range(3):
                if isPosAvailable(i, j) == True:
                    board[i][j] = comp
                    score = minimax(board, depth + 1, False)
                    board[i][j] = " "
                    bestScore = max(score, bestScore)
        return bestScore
    else:
        bestScore = 10000
        for i in range(3):
            for j in range(3):
                if isPosAvailable(i, j) == True:
                    board[i][j] = player
                    score = minimax(board, depth + 1, True)
                    board[i][j] = " "
                    bestScore = min(score, bestScore)
        return bestScore


def bestMove():
    bestScore = -10000

    for i in range(3):
        for j in range(3):
            if isPosAvailable(i, j) == True:
                board[i][j] = comp
                score = minimax(board, 0, False)
                board[i][j] = " "
                if score > bestScore:
                    bestScore = score
                    move = [i, j]
                    
    board[move[0]][move[1]] = comp
    button[move[0]][move[1]].config(text = comp)