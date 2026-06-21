class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:

        if max(grid) == 0:
            return 0
        
        q = collections.deque()
        directions = [(0,1), (0,-1), (1,0), (-1,0)]
        curr_area = 0
        max_area = 0

        rows = len(grid)
        cols = len(grid[0])

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    q.append((r,c))
                    grid[r][c] = 0
                    curr_area += 1

                    while q:
                        cell = q.pop()
                        
                        for dr, dc in directions:
                            nr, nc = cell[0] + dr, cell[1] + dc

                            if 0 <= nr < rows and 0 <= nc < cols:
                                if grid[nr][nc] == 1:
                                    q.append((nr,nc))
                                    grid[nr][nc] = 0
                                    curr_area += 1
                    
                    max_area = max(max_area, curr_area)
                    curr_area = 0
        
        return max_area


