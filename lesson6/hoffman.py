class Node:
    def __init__(self, weight=0.0, name='', left=None, right=None):
        self.weight = weight
        self.name = name
        self.left = left
        self.right = right
        self.l_visit = False
        self.r_visit = False

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
    while True:
        if tree.left and not tree.l_visit:
            leaves.update(add_path_to_leaves(get_leaves_code(tree.left), '0'))
            tree.l_visit = True
        elif tree.right and not tree.r_visit:
            leaves.update(add_path_to_leaves(get_leaves_code(tree.right), '1'))
            tree.r_visit = True
        else:
            if tree.name:
                leaves[tree.name] = ''
            return leaves


if __name__ == '__main__':
    nodes = []
    sum_ = 0
    elements = {'a1': 0.31, 'a2': 0.26, 'a3': 0.24, 'a4': 0.18, 'a5': 0.01}
    for i in elements:
        nodes.append(Node(elements[i], i))
    while len(nodes) != 1:
        node_sort(nodes)
        nodes.append(nodes.pop() + nodes.pop())
    leaves = get_leaves_code(nodes[0])
    for leaf in leaves:
        sum_ += len(leaves[leaf]) * elements[leaf]
    print(sum_)





