from faulthandler import disable
from tkinter import *
from tkinter import messagebox

root = Tk()
root.title('Tic Tac Toe')
count = 0
player1 = 'X'
player2 = 'O'


def disable_all_buttons():
    for i in t:
        for j in i:
            j.config(state=DISABLED)


def check_win():
    global count
    for i in range(3):
        if t[i][0]["text"] != ' ' and t[i][0]["text"] == t[i][1]["text"] and t[i][0]["text"] == t[i][2]["text"]:
            t[i][0].config(bg="red")
            t[i][1].config(bg="red")
            t[i][2].config(bg="red")
            winner = True
            disable_all_buttons()
            if t[i][0]["text"] == 'X':
                messagebox.showinfo(
                    "Tic Tac Toe", "CONGRATULATIONS! X Wins!!!")
            else:
                messagebox.showinfo(
                    "Tic Tac Toe", "CONGRATULATIONS! O Wins!!!")
            return
        if t[0][i]["text"] != ' ' and t[0][i]["text"] == t[1][i]["text"] and t[0][i]["text"] == t[2][i]["text"]:
            t[0][i].config(bg="red")
            t[1][i].config(bg="red")
            t[2][i].config(bg="red")
            disable_all_buttons()
            winner = True
            if t[0][i]["text"] == 'X':
                messagebox.showinfo(
                    "Tic Tac Toe", "CONGRATULATIONS! X Wins!!!")
            else:
                messagebox.showinfo(
                    "Tic Tac Toe", "CONGRATULATIONS! O Wins!!!")
            return

    if t[0][0]["text"] != ' ' and t[1][1]["text"] == t[0][0]["text"] and t[0][0]["text"] == t[2][2]["text"]:
        t[0][0].config(bg="red")
        t[1][1].config(bg="red")
        t[2][2].config(bg="red")
        disable_all_buttons()
        winner = True
        if t[0][0]["text"] == 'X':
            messagebox.showinfo("Tic Tac Toe", "CONGRATULATIONS! X Wins!!!")
        else:
            messagebox.showinfo("Tic Tac Toe", "CONGRATULATIONS! O Wins!!!")
        return

    if t[0][2]["text"] != ' ' and t[1][1]["text"] == t[0][2]["text"] and t[1][1]["text"] == t[2][0]["text"]:
        t[0][2].config(bg="red")
        t[1][1].config(bg="red")
        t[2][0].config(bg="red")
        disable_all_buttons()
        winner = True
        if t[0][2]["text"] == 'X':
            messagebox.showinfo("Tic Tac Toe", "CONGRATULATIONS! X Wins!!!")
        else:
            messagebox.showinfo("Tic Tac Toe", "CONGRATULATIONS! O Wins!!!")
        return

    # Check if tie
    if count == 9:
        messagebox.showinfo("Tic Tac Toe", "It's A Tie!\n No One Wins!")
        disable_all_buttons()
        return 0
    return 2


def checkWin(bot):
    for i in range(3):
        if t[i][0]["text"] == bot and t[i][0]["text"] == t[i][1]["text"] and t[i][0]["text"] == t[i][2]["text"]:
            return True
        if t[0][i]["text"] == bot and t[0][i]["text"] == t[1][i]["text"] and t[0][i]["text"] == t[2][i]["text"]:
            return True

    if t[0][0]["text"] == bot and t[1][1]["text"] == t[0][0]["text"] and t[0][0]["text"] == t[2][2]["text"]:
        return True
    if t[0][2]["text"] == bot and t[1][1]["text"] == t[0][2]["text"] and t[1][1]["text"] == t[2][0]["text"]:
        return True
    return False


def minimax(board, depth, isMaximizing):
    global count
    if checkWin(player2):
        return 1
    if checkWin(player1):
        return -1
    if depth == 9:
        return 0
    if isMaximizing:
        bestScore = -100
        for i in range(3):
            for j in range(3):
                if t[i][j]["text"] == ' ':
                    t[i][j]["text"] = player2
                    score = minimax(board, depth + 1, False)
                    t[i][j]["text"] = ' '
                    bestScore = max(score, bestScore)
        return bestScore
    else:
        bestScore = 10000
        for i in range(3):
            for j in range(3):
                if t[i][j]["text"] == ' ':
                    t[i][j]["text"] = player1
                    score = minimax(board, depth + 1, True)
                    t[i][j]["text"] = ' '
                    bestScore = min(score, bestScore)
        return bestScore


def b_click(b):
    global count
    if b["text"] == ' ':
        b["text"] = player1
        count = count + 1
        b.config(state=DISABLED)
        check_win()
    else:
        messagebox.showerror(
            "Tic Tac Toe", "Hey! That box has already been selected\nPick Another Box...")
        b.config(state=DISABLED)


def botMove():
    global count, t, player1, player2
    bestScore = -100
    bestMove = t[0][0]
    for i in t:
        for j in i:
            if (j["text"] == ' '):
                j["text"] = player2
                score = minimax(t, count + 1, False)
                j["text"] = ' '
                if (score > bestScore):
                    bestScore = score
                    bestMove = j
    bestMove["text"] = player2
    bestMove.config(state=DISABLED)
    count = count + 1
    check_win()


def start_commad(button):
    b_click(button)
    botMove()


def reset():
    global count
    global player1, player2
    global t
    count = 0
    role = messagebox.askquestion(
        "Start a new game", "Do you want to go first?")
    if role == "yes":
        player1 = 'O'
        player2 = 'X'

    # Build our buttons                width=6, bg="SystemButtonFace", command=lambda: start_commad(t[i][j]))
    b1 = Button(root, text=' ', font=("Helvetica", 25), height=3,
                width=6, bg="SystemButtonFace", command=lambda: start_commad(b1))
    b2 = Button(root, text=' ', font=("Helvetica", 25), height=3,
                width=6, bg="SystemButtonFace", command=lambda: start_commad(b2))
    b3 = Button(root, text=' ', font=("Helvetica", 25), height=3,
                width=6, bg="SystemButtonFace", command=lambda: start_commad(b3))

    b4 = Button(root, text=' ', font=("Helvetica", 25), height=3,
                width=6, bg="SystemButtonFace", command=lambda: start_commad(b4))
    b5 = Button(root, text=' ', font=("Helvetica", 25), height=3,
                width=6, bg="SystemButtonFace", command=lambda: start_commad(b5))
    b6 = Button(root, text=' ', font=("Helvetica", 25), height=3,
                width=6, bg="SystemButtonFace", command=lambda: start_commad(b6))

    b7 = Button(root, text=' ', font=("Helvetica", 25), height=3,
                width=6, bg="SystemButtonFace", command=lambda: start_commad(b7))
    b8 = Button(root, text=' ', font=("Helvetica", 25), height=3,
                width=6, bg="SystemButtonFace", command=lambda: start_commad(b8))
    b9 = Button(root, text=' ', font=("Helvetica", 25), height=3,
                width=6, bg="SystemButtonFace", command=lambda: start_commad(b9))
    t = [[b1, b2, b3], [b4, b5, b6], [b7, b8, b9]]
    if player1 == 'X':
        botMove()
    # Grid our buttons to the screen
    for i in range(3):
        for j in range(3):
            t[i][j].grid(row=i, column=j)


# Create my menu
my_menu = Menu(root)
root.config(menu=my_menu)

# Create Options menu
options_menu = Menu(my_menu, tearoff=False)
my_menu.add_cascade(label="Options", menu=options_menu)
options_menu.add_command(label="Rest Game", command=reset)


reset()

root.mainloop()
