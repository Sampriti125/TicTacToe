import random
L= [[" 1  |  2  | 3 "],["_____________"],[" 4  |  5  | 6 "],["_____________"],[" 7  |  8  | 9 "]]
for i in L:
    print(i[0])
l=[["    ","    ","    "],["    ","    ","    "],["    ","    ","    "]]
global count
global d
d=0
count=9
def con():
    global l
    global count
    l=[["    ","    ","    "],["    ","    ","    "],["    ","    ","    "]]
    res=input("Do you want to continue? [Y/N]:")
    if res.upper()=="Y":
        count=9
        player()
    elif res.upper()=="N":
        print("Thanks for playing!!")
    else:
        print("Enter valid answer.")
        con()
def check(player):
    return (
        l[0][0]==l[0][1]==l[0][2]==player or
        l[1][0]==l[1][1]==l[1][2]==player or
        l[2][0]==l[2][1]==l[2][2]==player or
        l[0][0]==l[1][0]==l[2][0]==player or
        l[0][1]==l[1][1]==l[2][1]==player or
        l[0][2]==l[1][2]==l[2][2]==player or
        l[0][0]==l[1][1]==l[2][2]==player or
        l[0][2]==l[1][1]==l[2][0]==player)
def player():
    def you():
        global count
        print("It's your move!")
        try:
            box=int(input("Which box do you want to enter?"))
            if box>=1 and box<=9:
                row = (box - 1) // 3
                col = (box - 1) % 3
                if l[row][col]=="    ":
                    l[row][col]=" X "
                    count=count-1
                else:
                    print("This box is taken. choose another box")
                    you()
            else:
                print("Please choose between 1-9 .")
                you()
        except:
            print("Please enter a number only")
            you()
        for r in l:
            print(r[0], r[1], r[2], sep="|")
            print("_____________")
        if check(" X "):
            print("Congratulations! You Won !!")
            con()
        elif count==0:
            print("This match is a draw.")
            con()
        else:
            ai()
    def ai():
        global count
        global empty
        print("Computer is making a move...")
        empty = []
        for i in range(3):
            for j in range(3):
                if l[i][j] == "    ":
                    empty.append((i, j))
        for i, j in empty:
            l[i][j] = " O "
            if check(" O "):
                 break
            l[i][j] = "    "
        else:
            for i, j in empty:
                l[i][j] = " X "
                if check(" X "):
                    l[i][j] = " O "
                    
                    break
                l[i][j] = "    "
            else:
                i, j = random.choice(empty)
                l[i][j] = " O "
        count=count-1
        for row in l:
            print(row[0], row[1], row[2], sep="|")
            print("_____________")
        if check(" O "):
            print("Computer Won. You lost.")
            con()
        elif count==0:
            print("This match is a draw.")
            con()
        else:
            you()
    you()
player()
    
        
        
        
    
            
            
