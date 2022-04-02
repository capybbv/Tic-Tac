from tkinter import *
from tkinter import messagebox

root = Tk()
root.title('Tic-Tac-Toe')


def b_click(b):
    if b["text"] == " ":
        b["text"] = player
        return True
    else:
        return False

def botauto(b):
    b["text"] = bot


def start_commad(number):
    if number == 1:
        if (b_click(Button_1) == True):
            addMove(player, 1)
            botMove()
        else:
            messagebox.showerror("Warning", "Already selected!\n")
    if number == 2:
        if (b_click(Button_2) == True):
            addMove(player, 2)
            botMove()
        else:
            messagebox.showerror("Warning", "Already selected!\n")
    if number == 3:
        if (b_click(Button_3) == True):
            addMove(player, 3)
            botMove()
            
        else:
            messagebox.showerror("Warning", "Already selected!\n")
    if number == 4:
        if (b_click(Button_4) == True):
            addMove(player, 4)
            botMove()
            
        else:
            messagebox.showerror("Warning", "Already selected!\n")
    if number == 5:
        if (b_click(Button_5) == True):
            addMove(player, 5)
            botMove()
            
        else:
            messagebox.showerror("Warning", "Already selected!\n")
    if number == 6:
        if (b_click(Button_6) == True):
            addMove(player, 6)
            botMove()
        else:
            messagebox.showerror("Warning", "Already selected!\n")
    if number == 7:
        if (b_click(Button_7) == True):
            addMove(player, 7)
            botMove()
        else:
            messagebox.showerror("Warning", "Already selected!\n")
    if number == 8:
        if (b_click(Button_8) == True):
            addMove(player, 8)
            botMove()
        else:
            messagebox.showerror("Warning", "Already selected!\n")
    if number == 9:
        if (b_click(Button_9) == True):
            addMove(player, 9)
            botMove()
            
        else:
            messagebox.showerror("Warning", "Already selected!\n")


def play_game():
    global board
    global player 
    global bot
    global Button_1, Button_2, Button_3, Button_4, Button_5, Button_6, Button_7, Button_8, Button_9
    board = {1: ' ', 2: ' ', 3: ' ',
             4: ' ', 5: ' ', 6: ' ',
             7: ' ', 8: ' ', 9: ' '}
    role = messagebox.askquestion("Start a new game", "Do you want to go first?")
    if role == 'yes':
        player = 'O'
        bot = 'X'
    else:
        player = 'X'
        bot = 'O' 


    Button_1 = Button(root, text=" ", font=("Helvetica", 30), height=3,
                width=6, bg="SystemButtonFace", command=lambda: start_commad(1))
    Button_2 = Button(root, text=" ", font=("Helvetica", 30), height=3,
                width=6, bg="SystemButtonFace", command=lambda: start_commad(2))
    Button_3 = Button(root, text=" ", font=("Helvetica", 30), height=3,
                width=6, bg="SystemButtonFace", command=lambda: start_commad(3))
    Button_4 = Button(root, text=" ", font=("Helvetica", 30), height=3,
                width=6, bg="SystemButtonFace", command=lambda: start_commad(4))
    Button_5 = Button(root, text=" ", font=("Helvetica", 30), height=3,
                width=6, bg="SystemButtonFace", command=lambda: start_commad(5))
    Button_6 = Button(root, text=" ", font=("Helvetica", 30), height=3,
                width=6, bg="SystemButtonFace", command=lambda: start_commad(6))
    Button_7 = Button(root, text=" ", font=("Helvetica", 30), height=3,
                width=6, bg="SystemButtonFace", command=lambda: start_commad(7))
    Button_8 = Button(root, text=" ", font=("Helvetica", 30), height=3,
                width=6, bg="SystemButtonFace", command=lambda: start_commad(8))
    Button_9 = Button(root, text=" ", font=("Helvetica", 30), height=3,
                width=6, bg="SystemButtonFace", command=lambda: start_commad(9))
    if (bot == 'O'):
        botMove()

    # Grid
    Button_1.grid(row=0, column=0)
    Button_2.grid(row=0, column=1)
    Button_3.grid(row=0, column=2)

    Button_4.grid(row=1, column=0)
    Button_5.grid(row=1, column=1)
    Button_6.grid(row=1, column=2)

    Button_7.grid(row=2, column=0)
    Button_8.grid(row=2, column=1)
    Button_9.grid(row=2, column=2)

def Check_Space(position):
    if board[position] == ' ':
        return True
    else:
        return False

def addMove(bot_or_player, position):
    if Check_Space(position):
        board[position] = bot_or_player
        if (checkDraw()):
            messagebox.showinfo("Tic Tac Toe", "Draw!!")
        if checkWin():
            if bot_or_player == bot:
                messagebox.showinfo("Tic Tac Toe", "You fail, bot wins!!")
            else:
                messagebox.showinfo("Tic Tac Toe", "Congratulations, you wins!!")
        return

def checkWin():
    if (board[1] == board[2] and board[1] == board[3] and board[1] != ' '):
        Button_1.config(bg="red")
        Button_2.config(bg="red")
        Button_3.config(bg="red")
        return True
    elif (board[4] == board[5] and board[4] == board[6] and board[4] != ' '):
        Button_4.config(bg="red")
        Button_5.config(bg="red")
        Button_6.config(bg="red")
        return True
    elif (board[7] == board[8] and board[7] == board[9] and board[7] != ' '):
        Button_7.config(bg="red")
        Button_8.config(bg="red")
        Button_9.config(bg="red")
        return True
    elif (board[1] == board[4] and board[1] == board[7] and board[1] != ' '):
        Button_1.config(bg="red")
        Button_4.config(bg="red")
        Button_7.config(bg="red")
        return True
    elif (board[2] == board[5] and board[2] == board[8] and board[2] != ' '):
        Button_2.config(bg="red")
        Button_5.config(bg="red")
        Button_8.config(bg="red")
        return True
    elif (board[3] == board[6] and board[3] == board[9] and board[3] != ' '):
        Button_3.config(bg="red")
        Button_6.config(bg="red")
        Button_9.config(bg="red")
        return True
    elif (board[1] == board[5] and board[1] == board[9] and board[1] != ' '):
        Button_1.config(bg="red")
        Button_5.config(bg="red")
        Button_9.config(bg="red")
        return True
    elif (board[7] == board[5] and board[7] == board[3] and board[7] != ' '):
        Button_3.config(bg="red")
        Button_5.config(bg="red")
        Button_7.config(bg="red")
        return True
    else:
        return False


def checkWin_tocalc(mark):
    if board[1] == board[2] and board[1] == board[3] and board[1] == mark:
        return True
    elif (board[4] == board[5] and board[4] == board[6] and board[4] == mark):
        return True
    elif (board[7] == board[8] and board[7] == board[9] and board[7] == mark):
        return True
    elif (board[1] == board[4] and board[1] == board[7] and board[1] == mark):
        return True
    elif (board[2] == board[5] and board[2] == board[8] and board[2] == mark):
        return True
    elif (board[3] == board[6] and board[3] == board[9] and board[3] == mark):
        return True
    elif (board[1] == board[5] and board[1] == board[9] and board[1] == mark):
        return True
    elif (board[7] == board[5] and board[7] == board[3] and board[7] == mark):
        return True
    else:
        return False


def checkDraw():
    for key in board.keys():
        if (board[key] == ' '):
            return False
    return True

def minimax(board, depth, isMaximizing):
    if (checkWin_tocalc(bot)):
        return 1
    elif (checkWin_tocalc(player)):
        return -1
    elif (checkDraw()):
        return 0

    if (isMaximizing):
        bestScore = -10
        for key in board.keys():
            if (board[key] == ' '):
                board[key] = bot
                score = minimax(board, depth + 1, False)
                board[key] = ' '
                if (score > bestScore):
                    bestScore = score
        return bestScore

    else:
        bestScore = 10
        for key in board.keys():
            if (board[key] == ' '):
                board[key] = player
                score = minimax(board, depth + 1, True)

                board[key] = ' '
                if (score < bestScore):
                    bestScore = score
        return bestScore


def botMove():
    bestScore = -10
    bestMove = 0
    for key in board.keys():
        if (board[key] == ' '):
            board[key] = bot
            score = minimax(board, 0, False)
            board[key] = ' '
            if (score > bestScore):
                bestScore = score
                bestMove = key
    if (bestMove == 1):
        Button_1["text"] = bot
    if (bestMove == 2):
        Button_2["text"] = bot
    if (bestMove == 3):
        Button_3["text"] = bot
    if (bestMove == 4):
        Button_4["text"] = bot
    if (bestMove == 5):
        Button_5["text"] = bot
    if (bestMove == 6):
        Button_6["text"] = bot
    if (bestMove == 7):
        Button_7["text"] = bot
    if (bestMove == 8):
        Button_8["text"] = bot
    if (bestMove == 9):
        Button_9["text"] = bot    
    addMove(bot, bestMove)
    return

my_menu = Menu(root)
root.config(menu=my_menu)

options_menu = Menu(my_menu)
my_menu.add_cascade(label="Options", menu=options_menu)
options_menu.add_command(label="Reset Game", command=play_game)

play_game()
root.mainloop()