import time
from ConsoleMethods import clearConsole, printSlow
from ConsoleMethods import movingDisplay
from Board import ShipBoard
from Board import AttackBoard
ruleStrings = ["The rules of Destroyer is simple", "The game begins with each player chosing where to place their ships",
    "On a 10 by 10 grid going from a-j and 1-10", "Each player will have 5 ships", "1 Carrier of length 5",
    "1 Battleship of length 4", "1 Cruiser of length 3", "1 Submarine of length 2", "1 Destroyer of length 1",
    "After all ships are placed for player 1 and 2","The first player will go on the attack",
    "This player will choose what square on the grind to attack ex a,1(top left corner)","If the attack hit player 1 goes again",
    "If it misses it is now player 2's turn","If player 2's attack his he goes again if not it's player 1's turn", "The game is over when one of the players have no ships remaining"]
def start():
    print("""8888888b.  8888888888  .d8888b.  88888888888 8888888b.   .d88888b.  Y88b   d88P 8888888888 8888888b.  
888  "Y88b 888        d88P  Y88b     888     888   Y88b d88P" "Y88b  Y88b d88P  888        888   Y88b 
888    888 888        Y88b.          888     888    888 888     888   Y88o88P   888        888    888 
888    888 8888888     "Y888b.       888     888   d88P 888     888    Y888P    8888888    888   d88P 
888    888 888            "Y88b.     888     8888888P"  888     888     888     888        8888888P"  
888    888 888              "888     888     888 T88b   888     888     888     888        888 T88b   
888  .d88P 888        Y88b  d88P     888     888  T88b  Y88b. .d88P     888     888        888  T88b  
8888888P"  8888888888  "Y8888P"      888     888   T88b  "Y88888P"      888     8888888888 888   T88b """)
    movingDisplay(10)
    for rule in ruleStrings:
        print(rule)
        time.sleep(0)
    time.sleep(0)
    clearConsole()


def main():
    start()
    player1DefBoard = ShipBoard(1,2)
    player2DefBoard = ShipBoard(2,1)
    player1OffenseBoard = AttackBoard(player2DefBoard)
    player2OffenseBoard = AttackBoard(player1DefBoard)
    time.sleep(0)
    player1DefBoard.setUp()
    clearConsole()
    input("Player 2 it is you're turn to set up you're board please press enter when ready:")
    player2DefBoard.setUp()
    clearConsole()
    player1Attack(player1OffenseBoard,player1DefBoard,player2OffenseBoard,player2DefBoard)

    
def player1Attack(player1Att:AttackBoard,player1Def:ShipBoard, player2Att:AttackBoard,player2Def:ShipBoard):
    clearConsole()
    if player1Att.points == 15:
        printSlow("Game over player 1 won")
        return    
    input("Player 1 it is you're turn to attack when you are ready press enter: ")
    if player1Att.attackPhase():
        player1Attack(player1Att,player1Def, player2Att,player2Def)
        return
    player2Attack(player2Att,player2Def,player1Att,player1Def)

def player2Attack(player2Att,player2Def,player1Att,player1Def):
    clearConsole()
    if player2Att.points == 15:
        printSlow("Game over player 2 won")
        return    
    input("Player 2 it is you're turn to attack when you are ready press enter: ")
    if player2Att.attackPhase():
        player2Attack(player2Att,player2Def,player1Att,player1Def)
        return
    player1Attack(player1Att,player1Def, player2Att,player2Def)
if __name__ == "__main__":
    main()

