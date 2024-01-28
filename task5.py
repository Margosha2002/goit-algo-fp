import uuid
import networkx as nx
import matplotlib.pyplot as plt


class Node:
    def __init__(self, key, color="skyblue"):
        self.left = None
        self.right = None
        self.val = key
        self.color = color
        self.id = str(uuid.uuid4())


def add_edges(graph, node, pos, x=0, y=0, layer=1):
    if node is not None:
        graph.add_node(node.id, color=node.color, label=node.val)
        if node.left:
            graph.add_edge(node.id, node.left.id)
            l = x - 1 / 2**layer
            pos[node.left.id] = (l, y - 1)
            l = add_edges(graph, node.left, pos, x=l, y=y - 1, layer=layer + 1)
        if node.right:
            graph.add_edge(node.id, node.right.id)
            r = x + 1 / 2**layer
            pos[node.right.id] = (r, y - 1)
            r = add_edges(graph, node.right, pos, x=r, y=y - 1, layer=layer + 1)
    return graph


def dfs_traversal(node, colors):
    if node is not None:
        colors[node.id] = get_color(len(colors))
        dfs_traversal(node.left, colors)
        dfs_traversal(node.right, colors)


def bfs_traversal(root, colors):
    queue = [root]
    while queue:
        node = queue.pop(0)
        if node is not None:
            colors[node.id] = get_color(len(colors))
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)


def get_color(index):
    shade = format(index % 256, "02X")
    color = f"#{shade}9{shade}F"
    print(color)
    return color


def draw_tree(tree_root, traversal_func):
    tree = nx.DiGraph()
    pos = {tree_root.id: (0, 0)}
    tree = add_edges(tree, tree_root, pos)

    colors = {}
    traversal_func(tree_root, colors)

    node_colors = [colors[node[0]] for node in tree.nodes(data=True)]
    labels = {node[0]: node[1]["label"] for node in tree.nodes(data=True)}

    plt.figure(figsize=(8, 5))
    nx.draw(
        tree,
        pos=pos,
        labels=labels,
        arrows=False,
        node_size=2500,
        node_color=node_colors,
    )
    plt.show()


root = Node(10)
root.left = Node(5)
root.left.left = Node(3)
root.left.right = Node(0)
root.right = Node(4)
root.right.left = Node(1)

draw_tree(root, dfs_traversal)

draw_tree(root, bfs_traversal)
