class Node:
    def __init__(self, weight=0.0, name='', left=None, right=None):
        self.weight = weight
        self.name = name
        self.left = left
        self.right = right

    def weight_return(self):
        return self.weight

    def __add__(self, other):
        return Node(self.weight + other.weight, left=self, right=other)


def node_sort(nodes):
    nodes.sort(key=Node.weight_return)
    nodes.reverse()


def add_path_to_leaves(leaves, number):
    if leaves:
        for i in leaves:
            leaves[i] += number
    return leaves


def get_leaves_code(tree):
    leaves = {}
    l_visit = False
    r_visit = False
    while True:
        if tree.left and not l_visit:
            leaves.update(add_path_to_leaves(get_leaves_code(tree.left), '0'))
            l_visit = True
        elif tree.right and not r_visit:
            leaves.update(add_path_to_leaves(get_leaves_code(tree.right), '1'))
            r_visit = True
        else:
            if tree.name:
                leaves[tree.name] = ''
            return leaves


def reverse_leaves(leaves):
    for i in leaves:
        leaves[i] = leaves[i][::-1]
    return leaves


def hoffman(elements):
    nodes = []
    for i in elements:
        nodes.append(Node(elements[i], i))
    while len(nodes) != 1:
        node_sort(nodes)
        nodes.append(nodes.pop() + nodes.pop())
    return reverse_leaves(get_leaves_code(nodes[0]))


if __name__ == '__main__':
    # nodes = []
    sum_ = 0
    elements_ = {'a1': 0.31, 'a2': 0.26, 'a3': 0.24, 'a4': 0.18, 'a5': 0.01}
    leaves = hoffman(elements_)
    print(leaves)
    for leaf in leaves:
        sum_ += len(leaves[leaf]) * elements_[leaf]
    print(sum_)





