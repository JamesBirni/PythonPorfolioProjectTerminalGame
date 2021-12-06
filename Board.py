from ConsoleMethods import clearConsole
from ConsoleMethods import printSlow
from UsefulMethods import listStringToInt
from Errors import ListNotEqual2
import time
class Board():
    aToJIntoNum = {"a":"1","b":"2","c":"3","d":"4","e":"5","f":"6","g":"7","h":"8","i":"9","j":"10"}
    def __init__(self):
        self.board =[[" ","a","b","c","d","e","f","g","h","i","j"],["1"],["2"],["3"],["4"],["5"],["6"],["7"],["8"],["9"],["10"]]
        for i in range(1,11):
            for j in range(1,11):
                self.nestedList = self.board[i]
                self.nestedList.append("■")
        self.usedXY = []
    def printBoard(self):
        printSlow('\n'.join([''.join(['{:4}'.format(item) for item in row]) 
      for row in self.board]))
    def userInputToXY(self, userInput):
        spiltUserInput = userInput.split(",")
        try:
            self.vaildInput(spiltUserInput)
            numUserInput = [Board.aToJIntoNum.get(spiltUserInput[0].lower()),spiltUserInput[1]]
            intUserInput = listStringToInt(numUserInput)
            return intUserInput
        except ListNotEqual2:
            printSlow("You didn't fromate that right try again")
            return["issue"]
    def xYInBounds(self, splitVar):     
        if 1 <=splitVar[0] <=10 and 1 <=splitVar[1] <=10:
            return True
        print(splitVar)
        printSlow("Thats not a number between 1 and 10")
        time.sleep(1.5)
        return False
    def vaildInput(self, lst):
        if len(lst) != 2:
            raise ListNotEqual2
        if not lst[1].isnumeric():
            printSlow(f"isn't numeric:{lst[1]}")
            raise ListNotEqual2
        if lst[0] not in ["a","b","c","d","e","f","g","h","i","j"]:
            raise ListNotEqual2
    
class ShipBoard(Board):
    shipLength = {"Carrier":5,"BattleShip":4,"Cruiser":3, "Submarine":2, "Destroyer":1}
    def __init__(self,playerNum:int,enemyNum:int):
        super().__init__()
        self.playerNum = playerNum
        self.enemyNum = enemyNum
        self.ships = {"Carrier":[[],[],[],[],[]],"BattleShip":[[],[],[],[]],"Cruiser":[[],[],[]], "Submarine":[[],[],[]], "Destroyer":[[]]}

    def setUpCurrentShip(self, ship:str):
        clearConsole()
        printSlow(f"Player {self.playerNum} please set up you're ships make sure player {self.enemyNum} does not see")
        self.printBoard()
        self.xYStart = input(f"Please input you're starting point for you're {ship} ex a,7: ")
        self.xYEnd = input(f"Please input you're ending point for you're ship \nThis must be in a stright line from you're starting point and {ShipBoard.shipLength.get(ship)} tiles apart: ")
        self.intXYStart =self.userInputToXY(self.xYStart)
        self.intXYEnd = self.userInputToXY(self.xYEnd)
        if self.intXYStart[0] == "issue" or self.intXYEnd[0] == "issue":
            self.setUpCurrentShip(ship)
            return
        if not self.xYInBounds(self.intXYStart) or not self.xYInBounds(self.intXYEnd):
            printSlow("Not in bounds")
            self.setUpCurrentShip(ship)
            return
        if self.intXYStart[0] != self.intXYEnd[0] and self.intXYStart[1] != self.intXYEnd[1]:
            printSlow("Those 2 start and end are on a diangle line please keep you're ships stright :)")
            self.setUpCurrentShip(ship)
            return
        if self.intXYStart[0] == self.intXYEnd[0] and self.intXYEnd[1]-self.intXYStart[1]+1 != ShipBoard.shipLength[ship]:
            if self.intXYStart[1]-self.intXYEnd[1]+1 != ShipBoard.shipLength[ship]:    
                printSlow("Looks like you're ship isn't gonna fit there try again")
                self.setUpCurrentShip(ship)
                return
        if self.intXYStart[1] == self.intXYEnd[1] and self.intXYEnd[0]-self.intXYStart[0]+1 != ShipBoard.shipLength[ship]:
            if self.intXYStart[0]-self.intXYEnd[0]+1 != ShipBoard.shipLength[ship]:     
                printSlow("Looks like you're ship isn't gonna fit there try again")
                self.setUpCurrentShip(ship)
                return
        self.x = self.intXYStart[0]
        self.y = self.intXYStart[1]
        self.lst = self.ships.get(ship)
        for count in range(0,ShipBoard.shipLength.get(ship)):
            if any([self.x,self.y] in x for x in self.usedXY):
                printSlow(f"There is a ships at {[self.x,self.y]} you cannot put you're {ship} here")
                self.setUpCurrentShip(ship)
                return
            self.lst[count].append(self.x)
            self.lst[count].append(self.y)
            self.board[self.y][self.x] = "□"
            print(self.lst)
            if self.intXYStart[0]-self.intXYEnd[0] > 0:
                self.x -=1
            elif self.intXYStart[0]-self.intXYEnd[0] < 0:
                self.x +=1
            if self.intXYStart[1]-self.intXYEnd[1] > 0:
                self.y -=1
            elif self.intXYStart[1]-self.intXYEnd[1] < 0:
                self.y += 1
        self.usedXY.append(self.lst)
        print(self.ships)
        self.lst = []

    
    def setUp(self):
        self.setUpCurrentShip("Carrier")
        self.setUpCurrentShip("BattleShip")
        self.setUpCurrentShip("Cruiser")
        self.setUpCurrentShip("Submarine")
        self.setUpCurrentShip("Destroyer")
        clearConsole()
        self.printBoard()
        time.sleep(3)
    
    def isShipThere(self,xy):
        printSlow(f"Used xy for def ship {self.usedXY}",8)
        if any([xy[0],xy[1]] in c for c in self.usedXY):return True
        return False
    def shipHit(self,xy):
        self.board[xy[0],xy[1]] = "▣"
        

class AttackBoard(Board):
    def __init__(self, enemyShipObject:ShipBoard):
        super().__init__()
        self.points = 0
        self.enemyShipObject = enemyShipObject
    def attackPhase(self):
        clearConsole()
        self.printBoard()
        self.xYString = input("Enter the X and Y you wish to attack ex, a,1: ")
        self.intXY = self.userInputToXY(self.xYString)
        if not self.xYInBounds(self.intXY):
            printSlow("This is not in bounds of a-j and 1-10")
            return self.attackPhase()
        printSlow(f"Used xy in attack{self.usedXY}")
        if any([self.intXY[0],self.intXY[1]] in i for i in self.usedXY):
            printSlow("We have already tried there")
            return self.attackPhase
        self.usedXY.append(self.intXY)
        if self.enemyShipObject.isShipThere(self.intXY):
            printSlow(f"This is X {self.intXY[0]} This is Y {self.intXY[1]}")
            self.board[self.intXY[0],self.intXY[1]] = "▣"
            printSlow("HIT")
            self.points +=1
            self.enemyShipObject.shipHit(self.intXY)
            return True
        printSlow("Miss")
        self.board[self.intXY[0]][self.intXY[1]] = "⧄"
        return False
        

        

