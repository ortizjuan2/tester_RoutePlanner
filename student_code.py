import networkx as nx
from queue import PriorityQueue
from math import sqrt

# get euclidean distance between two nodes
#
def get_cost(M, start_node, end_node):
    x,y = M._graph.node[start_node]['pos']
    x1,y1 = M._graph.node[end_node]['pos']
    return sqrt((x-x1)**2 + (y-y1)**2)

# A* implementation
#    
def shortest_path(M,start,goal):
    #print("shortest path called")
    frontier = PriorityQueue()
    # add tuble (priority, node) to priority queue
    frontier.put((0, start))
    camefrom = {}
    costsofar = {}
    camefrom[start] = None
    costsofar[start] = 0. 
    while not frontier.empty():
        cost, current = frontier.get()
        if current == goal:
            break
        for next_node in list(M._graph.edge[current].keys()):
            new_cost = costsofar[current] + get_cost(M, current, next_node)
            if next_node in costsofar:
                if new_cost < costsofar[next_node]:
                    costsofar[next_node] = new_cost
                    camefrom[next_node] = current
            else:
                costsofar[next_node] = new_cost
                camefrom[next_node] = current
                frontier.put((costsofar[next_node] + get_cost(M, next_node, goal), next_node))
    
    path = [goal]
    p = camefrom[goal]
    while p != None:
        path.append(p)
        p = camefrom[p]
    return path[::-1]



# brute force implementation
#
class brute_force(object):
    
    def __init__(self, M, start, goal):
        self.best_cost = 99999
        self.best_path = None
        self.total_cost = {}
        self.M = M
        self.start = start
        self.goal = goal

    def get_path(self, start, goal, cost, visited):
        #global best_cost
        #global best_path
        if start == goal:
            if cost < self.best_cost:
                self.best_cost = cost
                self.best_path = list(visited)
                init_cost = 0
                for i in range(1, len(visited)):
                    self.total_cost[visited[i]] = init_cost + get_cost(self.M, visited[i-1], visited[i])
                    init_cost = self.total_cost[visited[i]]
            return

        if start in self.total_cost:
            if self.total_cost[start] <= cost:
                return

        for next_node in list(self.M._graph.edge[start].keys()):
            if next_node not in visited:
                v = list(visited)
                v.append(next_node)
                new_cost = cost + get_cost(self.M, start, next_node)
                self.get_path(next_node, goal, new_cost, v)
        return
    
    
    



if __name__ == '__main__':
    import matplotlib.pyplot as plt
    import networkx as nx
    from helpers import Map, load_map
    
    M = load_map('map-40.pickle')
    G = M._graph
    labels = {}
    start = 8
    goal = 24
    path = shortest_path(M, start, goal)
    print("start: {} goal: {} path: {}".format(start, goal, path))
    for i in range(len(G.nodes())):
        labels[i] = str(i)

    pos=nx.spring_layout(G) # positions for all nodes
    nx.draw_networkx_nodes(G, pos, nodelist=M._graph.nodes(), node_color='r', node_size=500,
                            alpha=0.8)
    nx.draw_networkx_nodes(G,pos, nodelist=path, node_color='b', node_size=500, alpha=0.8)
    nx.draw_networkx_edges(G, pos, edgelist=G.edges(), width=1.0, alpha=0.5)
    nx.draw_networkx_labels(G, pos, labels, font_size=12)
    plt.axis('off')
    plt.show()
 
