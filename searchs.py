from time import sleep
import queue as Q

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

        node = queue.pop(0)

        if end_node.isEqual(node):
            print("end node found")
            return node
        else:
            node.setAsExpanded()
            neighbors_list = graph.get_neighbors(node)
            for neighbor in neighbors_list:
                #if neighbor.isNew():
                if  neighbor.isNew():
                    neighbor.setParent(node)
                    neighbor.setAsInlist()
                    queue.append(neighbor)
        sleep(0.01)
        interface.updateScreen()

    return None




def sc (graph,interface):

    start = graph.getStart_node()
    end = graph.getEnd_node()

   # if start not in graph:
    #    raise TypeError(str(start) + 'Não encontrado no grafo !')
     #   return
    #if end not in graph:
     #   raise TypeError(str(end) + ' Não encontrado no grafo !')
      #  return

    queue = []
    queue.append(start)

    while queue:
        node = queue.pop(0)
        #current = node[1][len(node[1]) - 1]

        if end.isEqual(node):
            #print("Caminho Encontrado: " + str(node[1]) + ", Custo = " + str(node[0]))
            return node

        #cost = node[0]
        node.setAsExpanded()
        for neighbor in graph.get_neighbors(node):
            if not neighbor.isParent_of(node):
            #temp = node[1][:]
                neighbor.setParent(node)
                neighbor.setCost(node.getCost() + 1)
                queue.append(neighbor)
                neighbor.setAsInlist()

        queue.sort(key=lambda no: no.getCost())
        interface.updateScreen()
            #queue.put((cost + graph[current][neighbor], temp))




search_dic = {0:(ds,'Deep Search'),
              1:(ws,'Wide Search'),
              2:(sc,'Cost Search ')}
