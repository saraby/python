import json


def construct_trees(nodes: list):
    """
    given the following list where the first item in the tuple is the node_id and
    the second item is the node_id of the parent; (NODE_ID, PARENT_NODE_ID)

    nodes = [
                ("node1", "node1"),
                ("node2", "node1"),
                ("node3", "node8"),
                ("node4", "node2"),
                ("node5", "node1"),
                ("node6", "node7"),
                ("node7", "node7"),
                ("node8", "node9"),
                ("node9", "node6"),
                ]

    create the following nested dict:

    {
        "node1": {
                    "node2": {
                                "node4":
                                        {

                                        }
                                },
                    "node5": {},

                    },
        "node7": {
                    "node6":{
                                "node9":
                                        {
                                            "node8":{
                                                        "node3":{}
                                                    }
                                        }
                                }

                    }

        }

    Restrictions
    1) place_node() should be a recusive function

    Tips!
        - let construct_trees() run until all nodes are places, or until there are no more
        nodes to place!
        - you might need a special condition to deal with the root of trees, e.g, nodes that have themselves as parents.

    """

    """
    Group 1. Collaboration with Klara, Marije, Sarab.
    """

    def place_node(d: dict, node):
        node_id, parent_id = node
        if node_id == parent_id:  # checks if this is a root
            d[parent_id] = {}  # place root nodes
            return True
        elif parent_id in d.keys():  # checks if parent node is already in the tree/subtrees
            d[parent_id][node_id] = {}  # places the nodes in the correct place
            return True
        for k in d:
            # checks all the keys of the subtree until parent_id is found
            if place_node(d[k], node):
                return True
        return False

    trees = {}
    while len(nodes) > 0:
        node = nodes.pop(0)
        if not place_node(trees, node):  # checks if it is possible to place node now
            nodes.append(node)  # puts back nodes that weren't placed yet
    return trees


if __name__ == '__main__':
    nodes = [
        ("node1", "node1"),
        ("node2", "node1"),
        ("node3", "node8"),
        ("node4", "node2"),
        ("node5", "node1"),
        ("node6", "node7"),
        ("node7", "node7"),
        ("node8", "node9"),
        ("node9", "node6"),
    ]

    print(json.dumps(construct_trees(nodes), indent=12, sort_keys=True))
