import const
import random
import copy



class Starter:
    def __init__(self):
        self.copyGrid = [[0]*9]*9
        self.grid = [[0]*9]*9
        self.answerGrid = [[1,4,7,2,5,8,6,9,3],[2,5,8,3,6,9,7,1,4],[3,6,9,4,7,1,8,2,5],[4,7,1,5,8,2,9,3,6],[5,8,2,6,9,3,1,4,7],[6,9,3,7,1,4,2,5,8],[7,1,4,8,2,5,3,6,9],[8,2,5,9,3,6,4,7,1],[9,3,6,1,4,7,5,8,2]]
        self.checker = SudokuSolver()
        self.shuffleAll()
        self.createStarter()



    def newGame(self,difficulty = 2):
        self.shuffleAll()
        self.createStarter(difficulty)



    def createStarter(self,difficulty = 2):
        x = random.randint(0,8)
        y = random.randint(0,8)
        for i in range(0,18,1):
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
            if(self.checker.onlyChoiceRule(self.grid)):
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
            x = random.randint(0,8)
            y = random.randint(0,8)




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


class SudokuSolver:
    def __init__(self):
        pass

    def zerosInRow(self,grid,index):
        count = 0
        for x in range(0,9,1):
            if(grid[x][index] == 0):
                count += 1
        return count

    def boxIndex(self,x,y):
        tempx = x - x%3
        tempy = y - y%3
        return (tempy + ((tempx+3)/3)) - 1

    def zerosInBox(self,grid,index):
        x = int((index % 3) * 3)
        y = int(index - (index % 3))
        box = []
        for i in range(x,x+3,1):
            for j in range(y,y+3,1):
                box.append(grid[i][j])
        return box.count(0)

    def onlyChoiceRule(self,grid):
        for x in range(0,9,1):
            temp = x
            if(x>4):
                temp = 8-x
            for y in range(0,temp+1,1):
                if(grid[x][y] == 0):
                    if(self.zerosInRow(grid,y)<2):#Row
                        pass
                    elif(grid[x].count(0)<2):#Column
                        pass
                    elif(self.zerosInBox(grid,self.boxIndex(x,y))<2):#Box
                        pass
                    else:
                        return False
        return True

    def singlePossibilityRule(self):
        pass

    def onlySquareRule(self):
        pass
