def ds(graph, start_node, end_node):
    stack = []
    stack.append(start_node)

    while(stack):

        node = stack.pop()

        if end_node == node:
            print("end node found")
            return node
        else:
            neighbors_list = graph.get_neighbors(node)
            for neighbor in neighbors_list:
                if not neighbor == node.getParent():
                    neighbor.setParent(node)
                    stack.append(neighbor)


    return None











def ds(graph,interface):
    stack = []
    start_node = graph.getStart_node()
    end_node = graph.getEnd_node()

    stack.append(start_node)

    while(stack):
        #print("ds inside while")
        node = stack.pop()

        if end_node.isEqual(node):
            print("end node found")
            return node
        else:
            node.setAsExpanded()
            neighbors_list = graph.get_neighbors(node)
            for neighbor in neighbors_list:
                if neighbor.isNew():
                    neighbor.setParent(node)
                    neighbor.setAsInlist()
                    stack.append(neighbor)
        sleep(0.01)
        interface.updateScreen()

    return None

#### search.py rep

def ds(graph, interface):
    stack = []
    start_node = graph.getStart_node()
    end_node = graph.getEnd_node()
    stack.append(start_node)

    while(stack):

        node = stack.pop()

        if end_node.isEqual(node):
            print("end node found")
            return node
        else:
            node.setAsExpanded()
            neighbors_list = graph.get_neighbors(node)
            for neighbor in neighbors_list:
                if neighbor.isNew():
                    neighbor.setParent(node)
                    neighbor.setAsInlist()
                    stack.append(neighbor)
        sleep(0.01)
        interface.updateScreen()

    return None

def ds2(graph, interface):
    stack = []
    start_node = graph.getStart_node()
    end_node = graph.getEnd_node()
    stack.append(start_node)

    while(stack):

        node = stack.pop()

        if end_node.isEqual(node):
            print("end node found")
            return node
        else:
            node.setAsExpanded()
            neighbors_list = graph.get_neighbors(node)
            for neighbor in neighbors_list:
                if not neighbor.isParent_of(node):
                    neighbor.setParent(node)
                    neighbor.setAsInlist()
                    stack.append(neighbor)
        sleep(0.01)
        interface.updateScreen()

    return None

def ws(graph,interface):
    queue = []
    start_node = graph.getStart_node()
    end_node = graph.getEnd_node()

    queue.append(start_node)

    while(queue):
        #print("ds inside while")
        node = queue.pop(0)

        if end_node.isEqual(node):
            print("end node found")
            return node
        else:
            node.setAsExpanded()
            neighbors_list = graph.get_neighbors(node)
            for neighbor in neighbors_list:
                if neighbor.isNew():
                    neighbor.setParent(node)
                    neighbor.setAsInlist()
                    queue.append(neighbor)
        sleep(0.01)
        interface.updateScreen()

    return None
