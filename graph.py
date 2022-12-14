class Node(object):
    def __init__(self, name, level, jump=None, required_item=None, inv={}, items={}):
        self.name = name
        self.level = level
        self.jump = jump
        self.required_item = required_item
        self.inventory = {items[k]:v for k, v in inv.items()}
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
            if not target.required_item or self.inventory[target.required_item]:
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
        if self.inventory[item]>0:
            if self.node.inventory[item]:
                self.node.inventory[item] += 1
            else:
                self.node.inventory[item] = 1
            self.inventory[item] -= 1
            
    def pick_up(self, item):
        if self.node.inventory[item]>0:
            if self.inventory[item]:
                self.inventory[item] += 1
            else:
                self.inventory[item] = 1
            self.node.inventory[item] -= 1

if __name__ == "__main__":

    items = {"Key":Item("Key")}

    a = Node("A", 0)
    b = Node("B", 1)
    c = Node("C", 1, "D")
    d = Node("D", 2, inv={"Key":1}, items=items)
    e = Node("E", 2, required_item=items["Key"])

    graph = {a:[b, c], b:[a], c:[a, d], d:[a,c,e], e:[d]}
    nodes = {node.name:node for node in graph.keys()}

    start_inv = {item:0 for item in items.values()}
    bob = Agent("Bob", a, [a, None, None, None, None, None], inventory=start_inv)

    print(bob.position)
    bob.move(nodes, graph, c)
    print(bob.position)
    bob.move(nodes, graph, d)
    print(bob.position)
    bob.pick_up(items["Key"])
    bob.move(nodes, graph, e)
    print(bob.position)
