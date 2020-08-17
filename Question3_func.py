import networkx as nx
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import graph_creator as gc

def createGraph(graph, path):
    """create AB-graph for Thor's movie
    input: networkx graph, reference to script
    output: networkx graph"""
    df = pd.read_excel(path)  # get data from xlsx file
    speaker = df['speaker']
    for i in range(len(speaker) - 2):
        if speaker[i] and speaker[i + 1]:
            graph.add_edge(speaker[i], speaker[i + 1])
    return graph


def createSubGraph(graph, path, characters_list):
    g = createGraph(graph, path)
    g2 = nx.subgraph(g, characters_list)
    return g2


def voting(g,path, characters, ancors):
    g = createSubGraph(g , path, characters)
    edge_matrix = np.zeros((len(characters), len(characters)))
    l = 0
    for i in characters:
        k = 0
        for j in characters:
            if g.has_edge(i, j):
                edge_matrix[l][k] = float(len(g.get_edge_data(i, j)))
            k += 1
        l += 1

    for i in range(len(edge_matrix)):
        edge_matrix[i][i] = 0
    for i in ancors:
        edge_matrix[i] = np.zeros(len(edge_matrix))
        edge_matrix[i][i] = 1

    k = 0
    for i in edge_matrix:
        if sum(i):
            edge_matrix[k] = (i / sum(i))
        else:
            edge_matrix[k] = 0
        k += 1

    for i in range(5000):
        edge_matrix = edge_matrix @ edge_matrix
    return edge_matrix


def voting_partition(edge_matrix, ancors):
    groups = dict()
    for i in ancors:
        groups[i] = list()

    k = 0
    for i in edge_matrix:
        if k in ancors:
            groups[k].append(k)
            k += 1
            continue
        highest_ancor = 0
        for j in range(len(i)):
            if i[j] > i[highest_ancor]:
                highest_ancor = j
        groups[highest_ancor].append(k)
        k += 1
    return groups


def vornoi(graph, path, characters, center_nodes):
    g = createSubGraph(graph, path, characters)
    return nx.voronoi_cells(g, center_nodes)

def translate_voting(g ,path, characters, ancors, dict_characters):
    d = dict()
    for i in voting_partition(voting(g ,path, characters, ancors), ancors).values():
        d[dict_characters[list(i)[0]]] = list()
        for j in i:
            d[dict_characters[list(i)[0]]].append(dict_characters[j])
    return d


def mst_partition(G, vornoi_partition, colors):
    red_edges = list(vornoi_partition)
    edge_colours = ['black' if not edge in red_edges else 'red'
                    for edge in G.edges()]
    black_edges = [edge for edge in G.edges() if edge not in red_edges]

    # Need to create a layout when doing
    # separate calls to draw nodes and edges
    pos = nx.spring_layout(G)
    nx.draw_networkx_nodes(G, pos, cmap=plt.get_cmap('jet'), node_size=500)
    nx.draw_networkx_labels(G, pos)
    nx.draw_networkx_edges(G, pos, edgelist=red_edges, edge_color='r', arrows=True)
    nx.draw_networkx_edges(G, pos, edgelist=black_edges, arrows=False)
    plt.show()


def paintGraph(g, color):
    """vizualization of a graph using mathplotlib library
    input: color (string)
    output: None"""

    options = {
        'node_color': color,
        'edge_color': color,
        'node_size': 100,
    }
    nx.draw(g, with_labels=True, **options)



g = nx.MultiDiGraph()
colors = ['green', 'black', 'blue', 'red']

# movie selected:
# path = 'xl_files/batman_begin.xlsx'
# characters = ['BATMAN', 'ALFRED', 'GORDON', 'DUCARD', 'FALCONE', 'FOX', 'RACHEL', 'CRANE', 'EARLE', 'FLASS']
# dict_characters = {0: 'BATMAN', 1: 'ALFRED', 2: 'GORDON', 3: 'DUCARD', 4: 'FALCONE', 5: 'FOX', 6: 'RACHEL',
#                    7: 'CRANE', 8:' EARLE', 9: 'FLASS'}
# center_nodes = {'BATMAN', 'DUCARD', 'FALCONE'}
# ancors = [0, 3, 4]

path = 'xl_files/thor.xlsx'
characters = ['THOR', 'HELA', 'LOKI', 'VALKYRIE', 'HULK', 'GRANDMASTER', 'SKURGE', 'HEIMDALL', 'SURTUR', 'ODIN']
dict_characters = {0: 'THOR', 1: 'HELA', 2: 'LOKI', 3: 'VALKYRIE', 4: 'HULK', 5: 'GRANDMASTER', 6: 'SKURGE',
                   7: 'HEIMDALL', 8: 'SURTUR', 9: 'ODIN'}
center_nodes = {'THOR', 'HELA', 'HULK'}
ancors = [0, 1, 4]

# # part d
# print('part d:')
vornoi_partition = vornoi(g, path, characters, center_nodes)
# print(vornoi_partition)
# vot_part = translate_voting(g, path, characters, ancors, dict_characters)
# print(vot_part)
g2 = createSubGraph(g, path, characters)
# print(nx.voterank(g2, 2))
# print('modularity: ',nx.modularity_spectrum(g2))

# # part g
mst_partition(g2, vornoi_partition, colors)