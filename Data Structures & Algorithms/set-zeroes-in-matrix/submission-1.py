class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:

        rows = len(matrix)
        cols = len(matrix[0])

        zRows = [False]*rows
        zCols = [False]*cols

        for row in range(rows):
            for col in range(cols):
                if matrix[row][col] == 0:
                    zRows[row] = True
                    zCols[col] = True
        
        for row in range(rows):
            for col in range(cols):
                if zCols[col] == True:
                    matrix[row][col] = 0
                
            if zRows[row] == True:
                for i in range(len(matrix[row])):
                    matrix[row][i] = 0
        
            



