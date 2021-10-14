from time import sleep


def getSerach_dic():
    return search_dic



def ws(graph,interface):
    stack = []
    start_node = graph.getStart_node()
    end_node = graph.getEnd_node()

    stack.append(start_node)

    while(stack):
        #print("ds inside while")
        node = stack.pop(0)

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

search_dic = {0:ds,
              1:ws}
