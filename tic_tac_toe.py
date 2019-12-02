board=list()
def init(board):
    for i in range(3):
        r=list()
        for j in range(3):
            r.append("| |")
        board.append(r)
def display(board):
    for i in range(3):
        for j in range(3):
            print(board[i][j],end="     ")
        print('\n\n')
def check(board,x,y,c):
    flag=0
    for i in range(3):
        if board[i][y]!=c:
            flag=1
            break
    if flag==0:
        return True
    flag=0
    for i in range(3):
        if board[x][i]!=c:
            flag=1
            break
    if flag==0:
        return True
    flag=0
    i=0
    j=0
    while i<3 and j<3:
        if board[i][j]!=c:
            flag=1
            break
        i+=1
        j+=1
    if flag==0:
        return True
    flag=0
    i=0
    j=2
    while i<3 and j>=0:
        if board[i][j]!=c:
            flag=1
            break
        i+=1
        j-=1
    if flag==0:
        return True
    return False
print("basic structure of input")
z=0
for i in range(3):
    for j in range(3):
        print("|{}|".format(z),end="    ")
        z+=1
    print("\n\n")
print("while you want to play press y")
d=input()
while d=='y':
    board=list()
    init(board)
    display(board)
    player1=input("you want to take X or O")
    player2='O'
    if player1=='X':
        player2='O'
    else:
        player2='X'
    c=0
    while c<9:
        if c%2==0:
            pos=int(input("player1: enter position (0-8) to insert"))
            board[(pos//3)][(pos%3)]=player1
            if check(board,(pos//3),(pos%3),player1):
                print("Player1 you won the Game!!!")
                break
        else:
            pos=int(input("player2: enter position (0-8) to insert"))
            board[(pos//3)][(pos%3)]=player2
            if check(board,(pos//3),(pos%3),player2):
                print("Player2 you won the Game!!!")
                break
        display(board)
        c+=1
    else:
        print("Draw")
    display(board)
    print("press y to continue playing")
    d=input()