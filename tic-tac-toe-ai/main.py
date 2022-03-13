from tkinter import *
from tkinter import messagebox

# to create the tkinter board window


def createBoard():
    global root, count, btnsList
    global b1, b2, b3, b4, b5, b6, b7, b8, b9
    count = 0
    root = Tk()
    root.title("Tic Tac Toe")
    root.configure(bg="white")
    lablel_1 = Label(root, text="Player (X)", height=3,
                     font=("COMIC SANS MS", 10, "bold"), bg="white")
    lablel_1.grid(row=0, column=1, columnspan=1)
    exit_button = Button(root, text="Quit", height=2, width=8,
                         font=("COMIC SANS MS", 10, "bold"), command=Quit)
    exit_button.grid(row=0, column=2, columnspan=1)
    b1 = Button(root, text="", height=4, width=8, bg="black", activebackground="white",
                fg="white", font="Times 15 bold", command=lambda: insert(b1, (0, 0)))
    b2 = Button(root, text="", height=4, width=8, bg="black", activebackground="white",
                fg="white", font="Times 15 bold", command=lambda: insert(b2, (0, 1)))
    b3 = Button(root, text="", height=4, width=8, bg="black", activebackground="white",
                fg="white", font="Times 15 bold", command=lambda: insert(b3, (0, 2)))
    b4 = Button(root, text="", height=4, width=8, bg="black", activebackground="white",
                fg="white", font="Times 15 bold", command=lambda: insert(b4, (1, 0)))
    b5 = Button(root, text="", height=4, width=8, bg="black", activebackground="white",
                fg="white", font="Times 15 bold", command=lambda: insert(b5, (1, 1)))
    b6 = Button(root, text="", height=4, width=8, bg="black", activebackground="white",
                fg="white", font="Times 15 bold", command=lambda: insert(b6, (1, 2)))
    b7 = Button(root, text="", height=4, width=8, bg="black", activebackground="white",
                fg="white", font="Times 15 bold", command=lambda: insert(b7, (2, 0)))
    b8 = Button(root, text="", height=4, width=8, bg="black", activebackground="white",
                fg="white", font="Times 15 bold", command=lambda: insert(b8, (2, 1)))
    b9 = Button(root, text="", height=4, width=8, bg="black", activebackground="white",
                fg="white", font="Times 15 bold", command=lambda: insert(b9, (2, 2)))
    b1.grid(row=2, column=0)
    b2.grid(row=2, column=1)
    b3.grid(row=2, column=2)
    b4.grid(row=3, column=0)
    b5.grid(row=3, column=1)
    b6.grid(row=3, column=2)
    b7.grid(row=4, column=0)
    b8.grid(row=4, column=1)
    b9.grid(row=4, column=2)
    btnsList = [b1, b2, b3, b4, b5, b6, b7, b8, b9]


# to create the list that would store the state of our game


def createBoardList():
    global boardList
    boardList = [["", "", ""], ["", "", ""], ["", "", ""]]

# to quit the tkinter 0board window


def Quit():
    global root
    msg = messagebox.askquestion("Confirm", "Are you sure you want to quit?")
    if msg == "yes":
        root.destroy()

# to close the tkinter winning window and tkinter board window


def Destruct():
    global winnerWindow
    winnerWindow.destroy()
    root.destroy()

# to start our game


def start():
    createBoard()
    createBoardList()
    moveAI()
    root.mainloop()

# to inserts X or O in the board


def insert(button, position):
    global count, root
    if button["text"] == "":
        if count % 2 != 0:
            button["text"] = "O"
            boardList[position[0]][position[1]] = "O"
            lablel_1 = Label(root, text="Player (X)", height=3, font=(
                "COMIC SANS MS", 10, "bold"), bg="white")
            lablel_1.grid(row=0, column=1, columnspan=1)
        count += 1
        if count >= 5:
            checkWinner()
        else:
            moveAI()
    else:
        messagebox.showinfo("Error", "This cell is already occupied")

# to check if we got a winner on the board


def checkWinner():
    global count
    if boardList[0][0] == boardList[0][1] == boardList[0][2] != "" or boardList[1][0] == boardList[1][1] == boardList[1][2] != "" or boardList[2][0] == boardList[2][1] == boardList[2][2] != "" or boardList[0][0] == boardList[1][0] == boardList[2][0] != "" or boardList[0][1] == boardList[1][1] == boardList[2][1] != "" or boardList[0][2] == boardList[1][2] == boardList[2][2] != "" or boardList[0][0] == boardList[1][1] == boardList[2][2] != "" or boardList[0][2] == boardList[1][1] == boardList[2][0] != "":
        if count % 2 == 0:
            displayWinner("Player (O)")
        else:
            displayWinner("Player (X)")
    elif count == 9:
        displayWinner("Tie")
    else:
        if count % 2 == 0:
            moveAI()


# to display the winning window


def displayWinner(winner):
    global t, winnerWindow
    winnerWindow = Tk()
    winnerWindow.title("Winner")
    winningLabel = Label(winnerWindow, width=32,
                         height=4, text="THE WINNER IS: ")
    winningLabel.pack()
    winningPlayerLabel = Label(winnerWindow, width=32, height=4, text=winner)
    winningPlayerLabel.pack()
    bproceed = Button(winnerWindow, text="Replay",
                      width=16, height=2, command=Reset)
    bproceed.pack()
    bproceed = Button(winnerWindow, text="Proceed",
                      width=16, height=2, command=Destruct)
    bproceed.pack()

# to reset the game again


def Reset():
    global count, boardList
    count = 0
    b1["text"] = ""
    b2["text"] = ""
    b3["text"] = ""
    b4["text"] = ""
    b5["text"] = ""
    b6["text"] = ""
    b7["text"] = ""
    b8["text"] = ""
    b9["text"] = ""
    boardList = [["", "", ""], ["", "", ""], ["", "", ""]]
    winnerWindow.destroy()
    createBoardList()
    moveAI()

# the computer move


def moveAI():
    global btnsList, boardList, count, root
    for btnIndex in range(len(btnsList)):
        if btnsList[btnIndex]["text"] == "":
            btnsList[btnIndex]["text"] = "X"
            position = getBtnPosition(btnIndex)
            boardList[position[0]][position[1]] = "X"
            lablel_1 = Label(root, text="Player (O)", height=3, font=(
                "COMIC SANS MS", 10, "bold"), bg="white")
            lablel_1.grid(row=0, column=1, columnspan=1)
            count += 1
            if count >= 5:
                checkWinner()
            break


def getBtnPosition(btnIndex):
    for i in range(3):
        for j in range(3):
            if i*3+j == btnIndex:
                return (i, j)


start()
