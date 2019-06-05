class SudokuSolver:
    def __init__(self):
        pass

    def Test(self,grid,level):
        if(self.gridRunThrough(grid,level)):
            return True
        return False






    def numberInRow(self,grid,index,number = 0):
        count = 0
        for x in range(0,9,1):
            if(grid[x][index] == number):
                count += 1
        return count

    def boxIndex(self,x,y):
        tempx = x - x%3
        tempy = y - y%3
        return (tempy + ((tempx+3)/3)) - 1

    def numberInBox(self,grid,index,number = 0):
        x = int((index % 3) * 3)
        y = int(index - (index % 3))
        box = []
        for i in range(x,x+3,1):
            for j in range(y,y+3,1):
                box.append(grid[i][j])
        print(box)
        return box.count(number)

    def beginnerRunThrough(self,grid,x,y):
        if(self.onlyChoiceRule(grid,x,y)):
            pass
        #elif(False):
        elif(self.singlePossibilityRule(grid,x,y)):
            pass
        else:
            return False
        return True

    def easyRunThrough(self,grid,x,y):
        pass

    def gridRunThrough(self,grid,level):
        for x in range(0,9,1):
            '''temp = x
            if(x>4):
                temp = 8-x
            for y in range(0,temp+1,1):'''
            for y in range(0,9,1):
                if(self.beginnerRunThrough(grid,x,y)):
                    pass
                else:
                    return False
        return True
                #if(level > 1):
                    #self.easyRunThrough(grid,x,y)



    def onlyChoiceRule(self,grid,x,y):
        if(grid[x][y] == 0):
            if(self.numberInRow(grid,y)<2):#Row
                pass
            elif(grid[x].count(0)<2):#Column
                pass
            elif(self.numberInBox(grid,self.boxIndex(x,y))<2):#Box
                pass
            else:
                return False
        return True

    def singlePossibilityRule(self,grid,x,y):
        if(grid[x][y] == 0):
            numbers = [False]*9

            for i in range(1,10,1):
                if(self.numberInRow(grid,y,i)>0):
                    numbers[i-1] = True
                elif(self.numberInBox(grid,self.boxIndex(x,y),i)>0):
                    numbers[i-1] = True
                elif(grid[x].count(i)>0):
                    numbers[i-1] = True
                else:
                    pass
            if(numbers.count(False)>1):
                return False
            else:
                return True

    def onlySquareRule(self,grid):
        if(grid[x][y] == 0):
            return False
