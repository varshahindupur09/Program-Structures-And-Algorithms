############################################################################################
1091: Leetcode
TC, SC :: O(N**2), O(N**2)

# why dijiktra's won't work in this case:
1. Dijkstra's algorithm would be necessary if:

2. The grid had varying weights for the paths (e.g., different terrains with different traversal costs).
There were other constraints or costs associated with reaching each cell beyond just counting steps.
############################################################################################
class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        # BFS - queue - fifo
        # edge cases
        if grid[0][0] != 0 or grid[-1][-1] != 0:
            return -1
        q = collections.deque()
        dir = [(0,-1),(1,0),(0,1),(-1,0),(-1,1),(1,-1),(1,1),(-1,-1)]
        # up , down, left, right = (0,-1),(1,0),(0,1),(-1,0) and rest are diagonals
        grid[0][0] = 1 # visited
        q.append((0,0,1))
        n = len(grid)

        while q:
            row, col, pathlength = q.popleft()
            # return output after traversing to the end
            if row == n - 1 and col == n - 1:
                return pathlength

            for dx, dy in dir:
                nx, ny = row + dx, col + dy
                
                if 0 <= nx < n and 0 <= ny < n and grid[nx][ny] == 0:
                    q.append((nx, ny, pathlength + 1))
                    grid[nx][ny] = 1 # visited

        # if no path was found
        return -1   



