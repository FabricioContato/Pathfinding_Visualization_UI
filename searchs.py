from time import sleep


def getSerach_dic():
    return search_dic

def node_in_list(lis,node):
    for in_list_node in lis:
        if in_list_node.isEqual(node):
            return True
    return False


def ds(graph, interface):
    stack = []
    start_node = graph.getStart_node()
    end_node = graph.getEnd_node()
    stack.append(start_node)

    while(stack):

        node = stack.pop()
        print(graph.heuristic_euclidean_distance(node))
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




search_dic = {0:(ds,'Deep Search'),
              1:(ws,'Wide Search')}
