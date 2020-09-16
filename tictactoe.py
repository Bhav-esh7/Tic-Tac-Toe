board=[' ' for x in range(10)]

def freespace(pos):
    return board[pos]==' '

def boardfull(board):
    if board.count(' ')>1:
        return False
    else:
        return True

def iswinner(b,l):
    return ((b[1]==l and b[2]==l and b[3]==l) or
    (b[4]==l and b[5]==l and b[6]==l) or
    (b[7]==l and b[8]==l and b[9]==l) or
    (b[1]==l and b[4]==l and b[7]==l) or
    (b[2]==l and b[5]==l and b[8]==l) or
    (b[3]==l and b[6]==l and b[9]==l) or
    (b[1]==l and b[5]==l and b[9]==l) or
    (b[3]==l and b[5]==l and b[7]==l) )

def insertLetter(letter,pos):
    board[pos]=letter

def printboard(board):
    print('   |   |   ')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('   |   |   ')
    print('------------')
    print('   |   |   ')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('   |   |   ')
    print('------------')
    print('   |   |   ')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('   |   |   ')

def playermove():


    run = True
    while run:
        move=input("Please select a position to enter between X between 1 to 9 ")
        try:
            move= int(move)
            if move>0 and move<10:
                if freespace(move):
                    run=False
                    insertLetter('X',move)
                else:
                    print("Sorry, this space is occupied ")
            else:
                print("Please enter a number between 1-9 ")
        
        except:
            print("Please type a number ")

def computermove():
    possiblemoves=[x for x, letter in enumerate(board) if letter==' ' and x!=0]
    move=0

    for let in ['O','X']:
        for i in possiblemoves:
            boardcopy=board[:]
            boardcopy[i]=let
            if iswinner(boardcopy, let):
                move=i
                return move
    
    cornerval=[]
    for i in possiblemoves:
        if i in [1,3,7,9]:
            cornerval.append(i)
    if len(cornerval)>0:
        move=selectrandom(cornerval)
        return move

    if 5 in possiblemoves:
        move=5
        return move

    edgeval=[]
    for i in possiblemoves:
        if i in [2,4,6,8]:
            edgeval.append(i)
    if len(edgeval)>0:
        move=selectrandom(edgeval)
        return move
    return move

def selectrandom(li):
    import random
    ln=len(li)
    r=random.randrange(0,ln)
    return li[r]

def maina():
    print("Welcome to the game!!!")
    printboard(board)

    while not(boardfull(board)):
        if not(iswinner(board,'O')):
            playermove()
            printboard(board)
        else:
            print("Sorry u lost the game :| ")
            break

        if not(iswinner(board,'X')):
            move=computermove()
            if move==0:
                print(" ")
            else:
                insertLetter('O',move)
                print("computer placed the O on position ", move, ":")
                printboard(board)
        else:
            print("Yay! You Won!!!")
            break

    if boardfull(board):
        print("No one won, The game will end in Tie")

while True:
    x=input("DO you want to play again? (y/n) ")
    if x.lower()=='y':
        board = [' ' for x in range(10)]
        print("------------")
        maina()
    else:
        break
