from framework import framework
from nodeGen import nodeGen

black = (0, 0, 0)

class pathFinding(framework):
    def __init__(self, grid, newSize, start, goals):
        super().__init__(grid, newSize, start, goals)
    
    def possibleActions(self, state):
        i, j = state
        actions = []

        if i >= 0 and j >= 0: 
            right, left = (i+1, j), (i-1, j)
            up, down = (i, j+1), (i, j-1) 

            if self.grid[right[0]][right[1]] != 4: actions.append(right)
            if self.grid[left[0]][left[1]] != 4: actions.append(left)
            if self.grid[up[0]][up[1]] != 4: actions.append(up)
            if self.grid[up[0]][up[1]] != 4: actions.append(down)
        return actions

    def goalState(self, state):
        return state in self.goalStates

    def stepCost(self, state, action):
        if len(state) == 1: 
            i, j = state[0][0], state[0][1]
        else:
            sX, sY = state[0], state[1]

        if action == "right": 
            aX, aY = 1, 0
        elif action == "left": 
            aX, aY = -1, 0
        elif action == "up": 
            aX, aY = 0, 1
        elif action == "down": 
            aX, aY = 0, -1

        new_x, new_y = sX + aX, sY + aY

        if new_x < 0 or new_x >= self.width or new_y < 0 or new_y >= self.height: 
            return float('inf')
        if self.grid[new_x][new_y] == black: 
            return float('inf')
        return 1

    def pathCost(self, goalNode):
        pathCost = 0
        currentNode = goalNode
        while currentNode.parent != None:
            pathCost += self.stepCost(currentNode.parent.state, currentNode.action)
            currentNode = currentNode.parent
        return pathCost
