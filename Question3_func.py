import networkx as nx
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

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
    g2 = nx.MultiGraph(nx.subgraph(g, characters_list))
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
        edge_matrix[k] = (i / sum(i))
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

def paintGraph(g, color):
    """vizualization of a graph using mathplotlib library
    input: networkx graph
    output: None"""

    options = {
        'node_color': 'gray',
        'edge_color': color,
        'node_size': 100,
        # 'font_color': '#d3aa78',
    }
    nx.draw(g, with_labels=True, **options)



g = nx.MultiGraph()
colors = ['green', 'black', 'blue', 'red']

path = 'xl_files/batman_begin.xlsx'
characters = ['BATMAN', 'ALFRED', 'GORDON', 'DUCARD', 'FALCONE', 'FOX', 'RACHEL', 'CRANE', 'EARLE', 'FLASS']
dict_characters = {0: 'BATMAN', 1: 'ALFRED', 2: 'GORDON', 3: 'DUCARD', 4: 'FALCONE', 5: 'FOX', 6: 'RACHEL',
                   7: 'CRANE', 8:' EARLE', 9: 'FLASS'}
center_nodes = {'BATMAN', 'DUCARD', 'FALCONE'}
ancors = [0, 3, 4]

# path = 'xl_files/thor.xlsx'
# characters = ['THOR', 'HELA', 'LOKI', 'VALKYRIE', 'HULK', 'GRANDMASTER', 'SKURGE', 'HEIMDALL', 'SURTUR', 'ODIN']
# center_nodes = {'THOR', 'HELA', 'HULK'}
# ancors = [0, 1, 4]

# part d
# print('part d:')
vornoi_partition = vornoi(g, path, characters, center_nodes)
print(vornoi_partition)
vot_part = translate_voting(g, path, characters, ancors, dict_characters)
print(vot_part)

# part g
g2 = createSubGraph(g, path, characters)
for i in vot_part.values():
    g4 = g2.subgraph(i)
    g5 = nx.minimum_spanning_tree(g4)
    paintGraph(g5, colors.pop())
plt.show()

