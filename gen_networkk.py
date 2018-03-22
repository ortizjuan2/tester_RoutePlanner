# graph generator v1.0
import networkx as nx 
from random import randint
from helpers import Map, load_map
import pickle
from bcolors import bcolors

TOTAL_NODES = 1000

def create_path(start, goal, num_nodes=10):
    '''
    Create a path starting from start upto goal
    incrementing apart nodes each time.

    Return: set of edges from start to goal
    '''
    nodes = goal - start
    apart = int(nodes / num_nodes)
    path = set()
    prev_node = start
    next_node = start +  apart
    # add nodes to the path from goal + aprt
    while next_node < goal:
        path.add((prev_node, next_node))
        prev_node = next_node
        next_node += apart
    # add last mile
    path.add((prev_node, goal))
    return path


if __name__ == '__main__':
    # generate nodes
    print('Starting node generation...'),
    nodes = [i for i in range(TOTAL_NODES)]
    print(bcolors.OKGREEN + '\t[DONE]' + bcolors.ENDC) 
    # create test network
    G = nx.Graph()
    G.add_nodes_from(nodes)
    edges = set()
    # generate edges from paths
    print('Starting edge generation...'),
    start = 0
    goal = TOTAL_NODES - 1
    for _ in range(int(TOTAL_NODES / 10)):
        num_nodes = randint(4, int(TOTAL_NODES/4))
        edges = edges.union(create_path(start, goal, num_nodes))
    G.add_edges_from(edges)
    print(bcolors.OKGREEN + '\t[DONE]' + bcolors.ENDC) 
    # generate nodes position
    attr = {}
    pos = set()
    print('Adding position attribute...'),
    while len(pos) < TOTAL_NODES:
        x = randint(0, TOTAL_NODES * 2)
        y = randint(0, TOTAL_NODES * 2)
        pos.add((x,y))
    i = 0
    for p in pos:
        attr[i] = p
        i += 1
    #set node position attribure
    nx.set_node_attributes(G, 'pos', attr)
    print(bcolors.OKGREEN + '\t[DONE]' + bcolors.ENDC) 
    fname = 'map-%s.pickle' % TOTAL_NODES
    # Serialize data to disk using pickle
    print('Saving file {} to disk...'.format(fname))
    with open(fname, 'wb') as f:
        pickle.dump(G, f, 2)
    print(bcolors.OKGREEN + '\t[DONE]' + bcolors.ENDC) 

