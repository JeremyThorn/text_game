class Node(object):
    def __init__(self, name, level, jump=None):
        self.name = name
        self.level = level
        self.jump = jump
    def __repr__(self):
        return self.name

class Agent(object):
    def __init__(self, name, node, position):
        self.node = node
        self.name = name
        self.position = position
    def move(self, nodes, graph, target):
        if target in graph[self.node]:
            if self.node.level > target.level:
                for level in range(self.node.level-target.level):
                    self.position[self.node.level-level] = None
            print(f"{self.name} moved from {self.node} to {target}.")
            self.node = target 
            self.position[self.node.level] = self.node
            if self.node.jump:
                self.move(nodes, graph, nodes[self.node.jump])            
        else:
            print(f"{self.name} could not move from {self.node} to {target}.\n{target} is not a neighbor of {self.node}.")

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
