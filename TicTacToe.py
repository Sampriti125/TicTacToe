import random
from rich.console import Console
console=Console()
from rich.table import Table
from rich import box
from rich.status import Status
import time
from rich.panel import Panel
text = """
[bold cyan]Welcome to Tic Tac Toe![/bold cyan]

[white]• You are[/white] [bold green]X[/bold green]
[white]• Computer is[/white] [bold blue]O[/bold blue]

[white]Enter a number (1–9) to place your move.[/white]
[dim]Refer to the board below for positions.[/dim]

[bold yellow]Try to beat the AI if you can 😈[/bold yellow]
"""
console.print(Panel(text, border_style="magenta"))
table = Table(
show_header=False, box=box.DOUBLE, show_lines=True, border_style="red")
for _ in range(3):
        table.add_column(justify="center")
table.add_row("1", "2", "3")
table.add_row("4", "5", "6")
table.add_row("7", "8", "9")
console.print(table)
l=[["    ","    ","    "],["    ","    ","    "],["    ","    ","    "]]
global count
def display():
    global box
    table = Table(
        show_header=False,
        box=box.SQUARE, show_lines=True)
    for _ in range(3):
        table.add_column(justify="center")

    for i in range(3):
        row = []
        for j in range(3):
            if l[i][j] == "    ":
                row.append(f"[dim]{i*3 + j + 1}[/dim]")
            elif l[i][j] == " X ":
                row.append("[bold green]X[/bold green]")
            else:
                row.append("[bold bright_blue]O[/bold bright_blue]")
        table.add_row(*row)

    console.print(table)
count=9
def con():
    global l
    global count
    l=[["    ","    ","    "],["    ","    ","    "],["    ","    ","    "]]
    console.print("Do you want to continue? [Y/N]: ", style="bold yellow",end="")
    res=input()
    if res.upper()=="Y":
        count=9
        player()
    elif res.upper()=="N":
        console.print("Thanks for playing!!", style="bold magenta")
    else:
        console.print("Enter valid answer.", style="bold yellow")
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
        console.print("It's your move!", style="bold cyan")
        try:
            console.print("Enter box number: ", style="bold blue",end="")
            box=int(input())
            if box>=1 and box<=9:
                row = (box - 1) // 3
                col = (box - 1) % 3
                if l[row][col]=="    ":
                    l[row][col]=" X "
                    count=count-1
                else:
                    console.print("This box is taken. choose another box", style="yellow")
                    you()
            else:
                console.print("Please choose between 1-9 .", style="yellow")
                you()
        except:
            console.print("Please enter a number only", style="yellow")
            you()
        display()
        if check(" X "):
            console.print("Congratulations! You Won !!", style="bright_red")
            con()
        elif count==0:
            console.print("This match is a draw.", style="bold white" )
            con()
        else:
            ai()
    def ai():
        global count
        global empty
        with console.status("[bold cyan]Computer is thinking..., [/bold cyan]", spinner="bouncingBar"):
            time.sleep(3)
        console.print("Computer has made it's move", style="bold cyan")
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
        display()
        if check(" O "):
            console.print("Computer Won. You lost.", style="bold bright_red")
            con()
        elif count==0:
            console.print("This match is a draw.", style="bold white")
            con()
        else:
            you()
    console.print(Panel("🎮 GAME START", style="bold green",border_style="magenta"))
    you()
player()
    
        
        
        
    
            
            
