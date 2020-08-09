import networkx as nx
import pandas as pd
import matplotlib.pyplot as plt
import re
import numpy as np


def unionSpeakers(speaker):
    """Merge different names of a character into one character
    input: dataFrame of characters
    output: list of characters"""
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
    """Calculate the number of edges (using multiplication matrices)
        and the number of nodes
        input: networkx graph
        output: integer tuple with the result"""
    adj_met = nx.to_numpy_matrix(g)
    nodes_num = len(adj_met)
    edges_num = (adj_met @ np.ones((len(adj_met))).transpose())/2 @ np.ones(len(adj_met)).transpose()
    return nodes_num, int(edges_num)


def printGraph(g):
    """vizualization of a graph using mathplotlib library
    input: networkx graph
    output: None"""
    nx.draw(g, with_labels=True)
    plt.show()


def get_centrality(movie_name, path):
    """select the 4 important characters according to 4 methods:
    closeness_centrality, degree_centrality, betweenness_centrality, eigenvector_centrality
    and print it to screen
    input: movie name and reference to xl file
    output: None"""
    g = [nx.MultiDiGraph(), nx.MultiGraph(), nx.DiGraph(), nx.Graph()]
    name = ['MultiDiGraph()', 'MultiGraph()', 'DiGraph()', 'Graph()']
    print('for the movie: ', movie_name)
    for graph_type, graph_name in zip(g, name):
        g1 = thorCreatGraph(graph_type, path)
        print(graph_name)
        print('closeness_centrality: ', sorted(nx.closeness_centrality(g1).items(),key=lambda x: x[1], reverse=True)[0:4])
        print('degree_centrality: ', sorted(nx.degree_centrality(g1).items(),key=lambda x: x[1], reverse=True)[0:4])
        if graph_name.__eq__('DiGraph()') or graph_name.__eq__('Graph()'):
            print('betweenness_centrality: ', sorted(nx.betweenness_centrality(g1).items(),key=lambda x: x[1], reverse=True)[0:4])
            print('eigenvector_centrality: ', sorted(nx.eigenvector_centrality(g1).items(),key=lambda x: x[1], reverse=True)[0:4])
        print()
    print()

# main
print('Question 2:')

print('part a,b')
print()
g = thorCreatGraph(nx.MultiGraph(), 'xl_files/script_thor.xlsx')
g2 = batmaCreateGraph(nx.MultiGraph(), 'xl_files/script_batman.xlsx')
printGraph(g)  # print AB graph
printGraph(g2)
print("Thor ragnarok characters: ", g.nodes)  # show the characters
print("Batman begin characters:", g2.nodes)
print()
print()

print('part c')
print('#nodes(left) & #edges(right) for "Thor ragnarok": ', count_edges_and_nodes(g))  # print #nodes(left) & #edges(right)
print('#nodes(left) & #edges(right) for "Batman begin": ', count_edges_and_nodes(g2))  # print #nodes(left) & #edges(right)
print()
print()

print('part d')
get_centrality('Thor ragnarok', 'xl_files/script_thor.xlsx')
get_centrality('Batman begin:', 'xl_files/script_batman.xlsx')
