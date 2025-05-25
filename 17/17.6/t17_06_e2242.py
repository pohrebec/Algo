def build_tree(nodes, layers):
    if not nodes:
        return None
    if len(nodes) == 1:
        return (nodes[0], None, None)

    last_layer_index = -1
    last_layer_nodes = set()
    for i in reversed(range(len(layers))):
        layer_set = set(layers[i])
        intersec = layer_set.intersection(nodes)
        if intersec:
            last_layer_index = i
            last_layer_nodes = intersec
            break

    root = list(last_layer_nodes)[0]
    left_nodes = [x for x in nodes if x < root]
    right_nodes = [x for x in nodes if x > root]
    left_subtree = build_tree(left_nodes, layers)
    right_subtree = build_tree(right_nodes, layers)
    return (root, left_subtree, right_subtree)

def preorder(tree):
    if tree is None:
        return ""
    root, left, right = tree
    return root + preorder(left) + preorder(right)

def main():
    layers = []
    while True:
        line = input().strip()
        if line == '*':
            break
        layers.append(line)

    all_nodes = set("".join(layers))
    tree = build_tree(sorted(all_nodes), layers)
    print(preorder(tree))

if __name__ == "__main__":
    main()

