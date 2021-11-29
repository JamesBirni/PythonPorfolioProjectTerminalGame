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
    def printBoard(self):
        print('\n'.join([''.join(['{:4}'.format(item) for item in row]) 
      for row in self.board]))
    def userInputToXY(self, userInput):
        spiltUserInput = userInput.split(",")
        try:
            self.listLen2(spiltUserInput)
            numUserInput = [Board.aToJIntoNum.get(spiltUserInput[0]),spiltUserInput[1]]
            intUserInput = listStringToInt(numUserInput)
            return intUserInput
        except ListNotEqual2:
            print("You didn't fromate that right try again")
            return["issue"]
    def xYInBounds(self, splitVar):     
        if 1 <=splitVar[0] <=10 and 1 <=splitVar[1] <=10:
            return True
        print(splitVar)
        print("Thats not a number between 1 and 10")
        time.sleep(1.5)
        return False
    def listLen2(self, lst):
        if len(lst) != 2:
            raise ListNotEqual2

class ShipBoard(Board):
    shipLength = {"Carrier":5,"BattleShip":4,"Cruiser":3, "Submarine":2, "Destroyer":1}
    def __init__(self):
        super().__init__()
        self.ships = {"Carrier":[[],[],[],[],[]],"BattleShip":[[],[],[],[]],"Cruiser":[[],[],[]], "Submarine":[[],[],[]], "Destroyer":[[]]}

    def setUpCurrentShip(self, ship):
        clearConsole()
        printSlow("Player 1 please set up you're ships make sure player 2 does not see")
        self.xYStart = input(f"Please input you're starting point for you're {ship} ex a,7")
        self.xYEnd = input(f"Please input you're ending point for you're ship \n this must be in a stright line from you're starting point and {ShipBoard.shipLength.get(ship)} tiles apart")
        self.intXYStart =self.userInputToXY(self.xYStart)
        self.intXYEnd = self.userInputToXY(self.xYEnd)
        if self.intXYStart[0] == "issue" or self.intXYEnd[0] == "issue":
            self.setUpCurrentShip(ship)
            return
        if not self.xYInBounds(self.intXYStart) or not self.xYInBounds(self.intXYEnd):
            #self.setUpCurrentShip(ship)
            return
        if self.intXYStart[0] != self.intXYEnd[0] and self.intXYStart != self.intXYEnd[0]:
            print("Those 2 start and end are on a diangle line please keep you're ships stright :)")
            #self.setUpCurrentShip(ship)
            return
        if self.intXYStart[0] == self.intXYEnd[0] and self.intXYEnd[1]-self.intXYStart[1]+1 != ShipBoard.shipLength[ship]:
            print("Looks like you're ship isn't gonna fit there try again")
            print(f"X start-end {self.intXYEnd[0]-self.intXYStart[0]}")
            print(f"Y start-end{self.intXYEnd[1]-self.intXYStart[1]}")
            #self.setUpCurrentShip(ship)
            return
        if self.intXYStart[1] == self.intXYEnd[1] and self.intXYEnd[0]-self.intXYStart[0]+1 != ShipBoard.shipLength[ship]:
            print("Looks like you're ship isn't gonna fit there try again")
            #self.setUpCurrentShip(ship)
            return
        self.x = self.intXYStart[0]
        self.y = self.intXYStart[1]
        for count in range(0,ShipBoard.shipLength.get(ship)):
            lst = self.ships.get(ship)
            lst[count].append(self.x)
            lst[count].append(self.y)
            print(lst)
            if self.intXYStart[0]-self.intXYEnd[0] > 0:
                self.x -=1
            elif self.intXYStart[0]-self.intXYEnd[0] < 0:
                self.x +=1
            if self.intXYStart[1]-self.intXYEnd[1] > 0:
                self.y -=1
            elif self.intXYStart[1]-self.intXYEnd[1] < 0:
                self.y += 1
        print(self.ships)

    
    def setUp(self):
        self.setUpCurrentShip("Carrier")
        #self.setUpCurrentShip("BattleShip")
        #self.setUpCurrentShip("Cruiser")
        #self.setUpCurrentShip("Submarine")
        #self.setUpCurrentShip("Destroyer")


