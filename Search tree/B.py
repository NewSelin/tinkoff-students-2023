from string import ascii_uppercase
class Edge:
    def __init__(self, par = None, children = None):
        self.par = par
        self.children = children
    def print(self, i):
        if isinstance(self, Leaf):
            l.append(self.data)
            return
        for C in self.children[:-1]:
            C.print(i+1)
            l.append(ascii_uppercase[i])
        self.children[-1].print(i + 1)


class Leaf(Edge):
    def __init__(self, data, par=None):
        super().__init__(par)
        self.data = data

    def insert(self, new_leaf):
        pass


class Node(Edge):
    def __init__(self, children, maxx, par=None):
        super().__init__(par, children)
        self.maxx = maxx
    def add_node(self, new_node):
        if len(self.children) < 3:
            new_node.par = self
            self.children.append(new_node)
            self.children.sort(key=lambda x: x.maxx)
            self.maxx = max(self.maxx, new_node.maxx)
        else:
            if self.par is None:
                new_par = Node([self], self.maxx)
                self.par = new_par
            if new_node.maxx < self.children[0].maxx:
                new_node2 = Node(self.children[1:], self.children[2].maxx)
                new_node.par = self
                self.children[1].par = new_node2
                self.children[2].par = new_node2
                self.children = [new_node, self.children[0]]
                self.maxx = self.children[1].maxx
            elif new_node.maxx < self.children[1].maxx:
                new_node2 = Node(self.children[1:], self.children[2].maxx)
                new_node.par = self
                self.children[1].par = new_node2
                self.children[2].par = new_node2
                self.children = [self.children[0], new_node]
                self.maxx = new_node.maxx
            elif new_node.maxx < self.children[2].maxx:
                new_node2 = Node([new_node, self.children[2]], self.children[2].maxx)
                new_node.par = new_node2
                self.children[2].par = new_node2
                self.children = self.children[:2]
                self.maxx = self.children[1].maxx
            else:
                new_node2 = Node([self.children[2], new_node], new_node.maxx)
                new_node.par = new_node2
                self.children[2].par = new_node2
                self.children = self.children[:2]
                self.maxx = self.children[1].maxx
            self.par.add_node(new_node2)
    def add_leaf(self, new_leaf):
        if len(self.children) < 3:
            new_leaf.par = self
            self.children.append(new_leaf)
            self.children.sort(key = lambda x: x.data)
            self.maxx = max(self.maxx, new_leaf.data)
        else:
            if self.par is None:
                new_par = Node([self], self.maxx)
                self.par = new_par
            if new_leaf.data < self.children[0].data:
                new_node = Node(self.children[1:], self.children[2].data)
                new_leaf.par = self
                self.children[1].par = new_node
                self.children[2].par = new_node
                self.children = [new_leaf, self.children[0]]
                self.maxx = self.children[1].data
            elif new_leaf.data < self.children[1].data:
                new_node = Node(self.children[1:], self.children[2].data)
                new_leaf.par = self
                self.children[1].par = new_node
                self.children[2].par = new_node
                self.children = [self.children[0], new_leaf]
                self.maxx = new_leaf.data
            elif new_leaf.data < self.children[2].data:
                new_node = Node([new_leaf, self.children[2]], self.children[2].data)
                new_leaf.par = new_node
                self.children[2].par = new_node
                self.children = self.children[:2]
                self.maxx = self.children[1].data
            else:
                new_node = Node([self.children[2], new_leaf], new_leaf.data)
                new_leaf.par = new_node
                self.children[2].par = new_node
                self.children = self.children[:2]
                self.maxx = self.children[1].data
            self.par.add_node(new_node)

    def insert(self, new_leaf):
        if isinstance(self.children[0], Leaf):
            self.add_leaf(new_leaf)
        elif self.children[0].maxx < new_leaf.data:
            if len(self.children) == 2:
                 self.children[1].insert(new_leaf)
            elif self.children[1].maxx < new_leaf.data:
                self.children[2].insert(new_leaf)
            else:
                 self.children[1].insert(new_leaf)
        else:
            self.children[0].insert(new_leaf)


class Tree:
    def __init__(self):
        self.root = None
    def insert(self, i):
        new_leaf = Leaf(i)
        if self.root is None:
            self.root = new_leaf
        elif isinstance(self.root, Leaf):
            new_node = Node(sorted([self.root, new_leaf], key = lambda x: x.data), max(self.root.data, i))
            self.root.par = new_node
            new_leaf.par = new_node
        else:
            self.root.insert(new_leaf)
        while self.root.par:
            self.root = self.root.par
    def print_tree(self):
        self.root.print(0)


n = int(input())
T = Tree()
lst = list(map(int, input().split()))
for i in lst:
    T.insert(i)
l = []
T.print_tree()
print(*l)