class Node(object):
    def __init__(self, name, level, jump=None, required_item=None, inventory={}):
        self.name = name
        self.level = level
        self.jump = jump
        self.required_item = required_item
        self.inventory = inventory
    def __repr__(self):
        return self.name

class Item(object):
    def __init__(self, name):
        self.name = name

class Agent(object):
    def __init__(self, name, node, position, inventory={}):
        self.node = node
        self.name = name
        self.position = position
        self.inventory = inventory
    def move(self, nodes, graph, target):
        if target in graph[self.node]:
            if self.inventory[target.required_item]:
                if self.node.level > target.level:
                    for level in range(self.node.level-target.level):
                        self.position[self.node.level-level] = None
                print(f"{self.name} moved from {self.node} to {target}.")
                self.node = target 
                self.position[self.node.level] = self.node
                if self.node.jump:
                    self.move(nodes, graph, nodes[self.node.jump])            
            else:    
                print(f"{self.name} could not move from {self.node} to {target}.\n{self.name} does not have the required items.")
        else:
            print(f"{self.name} could not move from {self.node} to {target}.\n{target} is not a neighbor of {self.node}.")
    def drop(self, item):
        if self.inventory[item]:
            if self.node.inventory[item]:
                self.node.inventory[item] += 1
            else:
                self.node.inventory[item] = 1
            if self.inventory[item] == 1:
                del self.inventory[item]
            else:
                self.inventory[item] -= 1
            
    def pick_up(self, item):
        if self.node.inventory[item]:
            if self.inventory[item]:
                self.inventory[item] += 1
            else:
                self.inventory[item] = 1
            if self.node.inventory[item] == 1:
                del self.node.inventory[item]
            else:
                self.node.inventory[item] -= 1

a = Node("A", 0)
b = Node("B", 1)
c = Node("C", 1, "D")
d = Node("D", 2)

nodes = {"A":a, "B":b, "C":c, "D":d}
graph = {a:[b, c], b:[a], c:[a, d], d:[a,c]}

bob = Agent("Bob", a, [a, None, None, None, None, None])

print(bob.position)
bob.move(nodes, graph, c)
print(bob.position)
bob.move(nodes, graph, d)
print(bob.position)
bob.move(nodes, graph, c)
print(bob.position)
bob.move(nodes, graph, a)
print(bob.position)
bob.move(nodes, graph, b)
print(bob.position)
