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
                if not neighbor.isExpanded():
                    neighbor.setParent(node)
                    neighbor.setAsInlist()
                    stack.append(neighbor)
        sleep(0.01)
        interface.updateScreen()


    return None
    
def ds3(graph, interface):
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
    
def ws2(graph,interface):
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
                if not neighbor.isExpanded():
                    neighbor.setParent(node)
                    neighbor.setAsInlist()
                    queue.append(neighbor)
        sleep(0.01)
        interface.updateScreen()

    return None
    
def ws3(graph,interface):
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
                if not neighbor.isParent_of(node):
                    neighbor.setParent(node)
                    neighbor.setAsInlist()
                    queue.append(neighbor)
        sleep(0.01)
        interface.updateScreen()

    return None


def aux_listPop(l):
    n = l[0]
    i = len(l)
    for i_, n_ in enumerate(l):
        if n_.getCost() > n.getCost():
            i = i_
            break
    l_aux = l[0:i]

    l_aux.sort(key=lambda n: sum([n.getCost(),-1 * n.getValue()]))

    node = l_aux.pop(0)
    l.remove(node)
    return node

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
        #node = aux_listPop(queue)
        node = queue.pop(0)
        print(node.getCost())
        #current = node[1][len(node[1]) - 1]

        if end.isEqual(node):
            #print("Caminho Encontrado: " + str(node[1]) + ", Custo = " + str(node[0]))
            return node

        #cost = node[0]
        node.setAsExpanded()
        for neighbor in graph.get_neighbors(node):
            #if not neighbor.isParent_of(node):
            if neighbor.isNew():
            #temp = node[1][:]

                #neighbor.setValue(graph.n_of_new_Neighbors(neighbor))
                neighbor.setParent(node,addParentCost=True)
                queue.append(neighbor)
                neighbor.setAsInlist()

        queue.sort(key=lambda no: no.getCost())
        sleep(0.01)
        interface.updateScreen()
            #queue.put((cost + graph[current][neighbor], temp))




search_dic = {0:(ds,'Deep Search (just new nodes)'),
              1:(ds2,'Deep Search (no expanded nodes)'),
              2:(ds3,'Deep Search (no parent)'),
              3:(ws,'Wide Search (just new nodes)'),
              4:(ws2,'Wide Search (no expanded nodes)'),
              5:(ws3,'Wide Search (no parent)'),
              6:(sc,'Cost Search ')}
