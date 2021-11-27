class Board():
    aToJIntoNum = {"a":"1","b":"2","c":"3","d":"4","e":"5","f":"6","g":"7","h":"8","i":"9","j":"10"}
    def __init__(self):
        self.board =[["a","b","c","d","e","f","g","h","i","j"],["1"],["2"],["3"],["4"],["5"],["6"],["7"],["8"],["9"],["10"]]
        for i in range(1,11):
            for j in range(1,11):
                self.board[i][j] ="■"
