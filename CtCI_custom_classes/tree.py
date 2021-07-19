class Tree:
    def __init__(self, key=None, children=None):
        if children is None:
            children = []
        self.root = key
        self.children = children

    def get_root(self):
        return self.root

    def set_root(self, key):
        self.root = key

    def get_children(self):
        return self.children

    def set_children(self, children=None):
        if children is None:
            children = []
        self.children = children

    def __str__(self, level=0, depth=0):
        if depth == 0:
            depth = self.get_depth()
        ret = '\t' * level + repr(self.get_root()) + ('___' * depth) + '\n'
        for child in self.get_children():
            if child is None:
                ret += ("\t" * (level+1)) + '|\n'
            else:
                ret += child.__str__(level + 1, depth - 1)
        return ret

    def __repr__(self):
        return '<tree node representation>'

    def get_depth(self):
        d = 1
        if self.get_children() is None:
            return d
        for c in self.get_children():
            if c is not None:
                d = max(d, c.get_depth() + 1)
        return d
