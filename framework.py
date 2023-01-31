
from abc import ABC, abstractmethod
from nodeGen import nodeGen


class framework(ABC):
    def __init__(self, grid, newSize, start, goals):
        self.grid, self.newSize = grid, newSize
        self.start = start
        self.goals = goals
        self.width, self.height = len(grid), len(grid[0])
        self.start, self.goalStates = start, goals

    @abstractmethod
    def possibleActions(self, state): pass

    @abstractmethod
    def goalState(self, state): pass

    @abstractmethod
    def stepCost(self, state, action): pass

    @abstractmethod 
    def pathCost(self, goalNode): pass

