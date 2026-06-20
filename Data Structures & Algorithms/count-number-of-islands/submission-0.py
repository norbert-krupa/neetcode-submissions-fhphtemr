class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        q = collections.deque()
        directions = [(0,1), (0,-1), (1,0), (-1,0)]
        rows = len(grid)
        cols = len(grid[0])
        islands = 0

        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == "1":
                    q.append((i,j))

                    while q:
                        cell = q.pop()

                        for dr, dc in directions:
                            nr, nc = cell[0] + dr, cell[1] + dc



                            if 0 <= nr < rows and 0 <= nc < cols:
                                if grid[nr][nc] == "1":
                                    q.append((nr,nc))
                        
                        grid[cell[0]][cell[1]] = "0"
                    
                    islands += 1
        
        return islands

                        

