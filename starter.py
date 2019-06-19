import const
import random
import sudokusolver
import copy



class Starter:
    def __init__(self):
        self.copyGrid = [[0]*9]*9
        self.grid = [[0]*9]*9
        self.answerGrid = [[1,4,7,2,5,8,6,9,3],[2,5,8,3,6,9,7,1,4],[3,6,9,4,7,1,8,2,5],[4,7,1,5,8,2,9,3,6],[5,8,2,6,9,3,1,4,7],[6,9,3,7,1,4,2,5,8],[7,1,4,8,2,5,3,6,9],[8,2,5,9,3,6,4,7,1],[9,3,6,1,4,7,5,8,2]]
        self.checker = sudokusolver.SudokuSolver()
        self.shuffleAll()
        self.createStarter()
        self.hint = False



    def newGame(self,difficulty = 1):
        self.shuffleAll()
        self.createStarter(difficulty)

    def giveHint(self,coord):
        if(not self.hint):
            self.hint = True
            return answerGrid[coord[0]][coord[1]]
        else:
            return 0

    def createStarter(self,difficulty = 1):
        x = random.randint(0,8)
        y = random.randint(0,8)
        for i in range(0,20,1):
            if(x == y and (x + y) == 8):
                self.grid[x][y] = 0
            elif(x == y):
                self.grid[x][y] = 0
                self.grid[-1*(y+1)][-1*(x+1)] = 0
            elif(x + y == 8):
                self.grid[x][y] = 0
                self.grid[y][x] = 0
            else:
                self.grid[x][y] = 0
                self.grid[y][x] = 0
                self.grid[-1*(y+1)][-1*(x+1)] = 0
                self.grid[-1*(x+1)][-1*(y+1)] = 0

            self.checkRules(x,y,difficulty)

            x = random.randint(0,8)
            y = random.randint(0,8)

    def checkRules(self,x,y,difficulty):
        if(self.checker.Test(self.grid,difficulty)): # Move to Sudoku Solver class
            pass
        else:
            if(x == y and (x + y) == 8):
                self.grid[x][y] = self.answerGrid[x][y]
            elif(x == y):
                self.grid[x][y] = self.answerGrid[x][y]
                self.grid[-1*(y+1)][-1*(x+1)] = self.answerGrid[-1*(y+1)][-1*(x+1)]
            elif(x + y == 8):
                self.grid[x][y] = self.answerGrid[x][y]
                self.grid[y][x] = self.answerGrid[y][x]
            else:
                self.grid[x][y] = self.answerGrid[x][y]
                self.grid[y][x] = self.answerGrid[y][x]
                self.grid[-1*(y+1)][-1*(x+1)] = self.answerGrid[-1*(y+1)][-1*(x+1)]
                self.grid[-1*(x+1)][-1*(y+1)] = self.answerGrid[-1*(x+1)][-1*(y+1)]


    def shuffleAll(self):
        shuffler = random.randint(0,1)
        if(shuffler == 1):
            self.transposeGrid()
            self.answerGrid = copy.deepcopy(self.copyGrid)
        self.shuffleLists(self.answerGrid)
        self.shuffleBoxes(self.answerGrid)
        self.transposeGrid()
        self.shuffleLists(self.copyGrid)
        self.shuffleBoxes(self.copyGrid)
        self.untransposeGrid()
        self.grid = copy.deepcopy(self.answerGrid)

    def shuffleBoxes(self,source):
        box = [[[0]*9]*3]*3
        for i in range(0,3,1):
            box[i] = source[i*3:i*3+3]
        random.shuffle(box)
        for i in range(0,9,1):
            source[i] = box[int((i-(i%3))/3)][i%3]

    def transposeGrid(self):
        self.copyGrid = [[self.answerGrid[j][i]for j in range(len(self.answerGrid))] for i in range(len(self.answerGrid[0]))]

    def untransposeGrid(self):
        self.answerGrid = [[self.copyGrid[j][i]for j in range(len(self.copyGrid))] for i in range(len(self.copyGrid[0]))]

    def shuffleLists(self,source):
        for i in range(0,9,3):
            temp = source[i:i+3]
            random.shuffle(temp)
            for j in range(i,i+3,1):
                source[j] = temp[j-i]
