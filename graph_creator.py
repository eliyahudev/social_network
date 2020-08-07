import networkx as nx
import pandas as pd
import matplotlib.pyplot as plt
import re
import numpy as np


def unionSpeakers(speaker):
    new_speaker = dict()
    j = 0
    for i in speaker:
        if str(i).__eq__('nan'):
            continue
        new_speaker[j] = i
        if re.search('YOUNG BRUCE|WAYNE|BRUCE', i):
            new_speaker[j] = 'BATMAN'
        if re.search('DUCARD/RA\'S AL GHUL|RA\'S AL GHUL', i):
            new_speaker[j] = 'DUCARD'
        j += 1
        # print(benshelzona)
    return new_speaker


def batmaCreateGraph(g, script):
    """create AB-graph for Batman's movie
    input: networkx graph, reference to script
    output: networkx graph"""
    # get data from xlsx file
    script_df = pd.read_excel(script)
    speaker = unionSpeakers(script_df['speaker'])
    # addin edges to the graph
    for i in range(len(speaker) - 1):
        g.add_edge(speaker[i], speaker[i + 1])
    return g


def thorCreatGraph(g, script):
    """create AB-graph for Thor's movie
    input: networkx graph, reference to script
    output: networkx graph"""
    # get data from xlsx file
    script_df = pd.read_excel(script)
    speaker = script_df['speaker']
    for i in range(len(speaker) - 1):
        g.add_edge(speaker[i], speaker[i + 1])
    return g


def count_edges_and_nodes(g):
    adj_met = nx.to_numpy_matrix(g)
    nodes_num = len(adj_met)
    edges_num = (np.ones((len(adj_met))).transpose() @ adj_met) @ np.ones(len(adj_met))
    return nodes_num, int(edges_num)


def printGraph(g):
    """vizualization of a graph using mathplotlib library
    input: networkx graph
    output: None"""
    nx.draw(g, with_labels=True)
    plt.show()


# main
g = thorCreatGraph(nx.MultiGraph(), 'xl_files/script_thor.xlsx')
printGraph(g)  # print AB graph
print(count_edges_and_nodes(g))  # print #nodes(left) & #edges(right)

g = batmaCreateGraph(nx.MultiGraph(), 'xl_files/script_batman.xlsx')
printGraph(g)  # print AB graph
print(count_edges_and_nodes(g))  # print #nodes(left) & #edges(right)
