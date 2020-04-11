import os
clear = lambda: os.system('clear')

lr = "  A B C"
board = ["1", " _", " _", " _", "2", " _", " _", " _", "3", " _", " _", " _"]
g_end = False
movelog = []
movelist = {"a1": 1, "b1": 2, "c1": 3, "a2": 5, "b2": 6, "c2": 7, "a3": 9, "b3": 10, "c3": 11}

def iswin(letter):
    if ((board[1] == letter and board[2] == letter and board[3] == letter) or \
    (board[5] == letter and board[6] == letter and board[7] == letter) or \
    (board[9] == letter and board[10] == letter and board[11] == letter) or \
    (board[1] == letter and board[5] == letter and board[9] == letter) or \
    (board[2] == letter and board[6] == letter and board[10] == letter) or \
    (board[3] == letter and board[7] == letter and board[11] == letter) or \
    (board[1] == letter and board[6] == letter and board[11] == letter) or \
    (board[3] == letter and board[6] == letter and board[9] == letter)):
        return True

while True:
    p1 = input("Would you like to play as X or O ?(X/O) ")
    if p1.lower() in ["x", "o"]:
        if p1 == "x":
            p1 = " X"
            p2 = " O"
        else:
            p1 = " O"
            p2 = " X"
        break
    else:
        print("Please select 'X' or 'O'")

clear()
print("Player 1 is " + p1)
print("Player 2 is " + p2)

while True:
    cp = (input("Would you like to make the first move?(Yes/No) ")).lower()
    if cp in ["yes", "no"]:
        if cp == "yes":
            cp = True
            clear()
            print("Player 1 will go first.")
        else:
            cp = False
            clear()
            print("Player 2 will go first.")
        break
    else:
        print("Please select 'Yes' or 'No'")

while g_end != True:
    clear()
    print("\n" + lr)
    print(''.join(board[0:4]))
    print(''.join(board[4:8]))
    print(''.join(board[8:]))
    if cp == True:
        action = (input("\n Player 1's Move (A-B, 1-3): ")).lower()
    if cp == False:
        action = (input("\n Player 2's Move (A-B, 1-3): ")).lower()
    if action in movelog:
        print("That slot is already filled.")
    elif action not in movelist:
        print("Invalid move.")
    else:
        movelog.append(action)
        if cp == True:
            board[movelist[action]] = (p1)
            if iswin(p1):
                g_end = True
                winner = "Player 1"
            cp = False
        else:
            board[movelist[action]] = (p2)
            if iswin(p2):
                g_end = True
                winner = "Player 2"
            cp = True

print("\nGame Over!")
print(winner + " Has Won!")
