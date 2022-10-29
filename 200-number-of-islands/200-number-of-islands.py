class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        def dfs(grid,i,j):
            if i < 0 or j < 0 or i>= len(grid) or j>= len(grid[0]) or grid[i][j]!='1':
                return
            # condition d'arret index out of range or the grid isn't 1 so we reached the end of the island 
            
            grid[i][j] = "#"
            dfs(grid,i+1,j) #searching for the end of the island
            dfs(grid,i-1,j)
            dfs(grid,i,j+1)
            dfs(grid,i,j-1)
            
            
        count = 0
        if not grid :
            return 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    
                    dfs(grid,i,j) # mark all adjacent 1 by '#'
                    count+=1
        return count
                
                        
                        