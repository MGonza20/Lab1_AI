
# Referencia: AI a modern aproach - Page 79

class nodeGen():
    def __init__(self, parent, action, pathCost, state):
        self.parent = parent
        self.action = action
        self.pathCost = pathCost
        self.state = state