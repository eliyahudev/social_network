import matplotlib.pyplot as plt
import networkx as nx
import numpy as np
import pandas as pd
import time

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
    g2 = createGraph(graph, path)
    g3 = g2.copy()
    for i in g2.nodes():
        if not str(i) in characters_list:
            g3.remove_node(i)
    return g3


def voting(g, path, characters, ancors):
    g = createSubGraph(g, path, characters)
    edge_matrix = nx.to_numpy_array(g)

    for i in range(len(edge_matrix)):
        edge_matrix[i][i] = 0

    for i in ancors:
        edge_matrix[i] = np.zeros(len(edge_matrix))
        edge_matrix[i][i] = 1

    k = 0
    for i in edge_matrix:
        if sum(i) != 0:
            edge_matrix[k] = (i / sum(i))
        else:
            edge_matrix[k] = 0
        k += 1

    for i in range(50000):
        edge_matrix = edge_matrix.dot(edge_matrix)

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


def translate_voting(g, path, characters, ancors, dict_characters):
    d = dict()
    for i in voting_partition(voting(g, path, characters, ancors), ancors).values():
        d[dict_characters[list(i)[0]]] = list()
        for j in i:
            d[dict_characters[list(i)[0]]].append(dict_characters[j])
    return d


def mst_partition(G, vornoi_partition, colors, center_nodes):
    print(vornoi_partition)
    red_edges = vornoi_partition[center_nodes[0]]
    # separate calls to draw nodes and edges
    rd_edges = [edge for edge in G.edges() if edge[1] in red_edges and edge[0] in red_edges]
    black_edges = [edge for edge in G.edges() if not edge[1] in red_edges and not edge[0] in red_edges]

    # fig = plt.figure(figsize=(50, 50))
    pos = nx.circular_layout(G, scale=0.2)
    # pos[0] = np.array([-10,-10])
    nx.draw_networkx_edges(G, pos, edgelist=rd_edges, width=2, edge_color='r', arrows=True, label=True)
    nx.draw_networkx_edges(G, pos, edgelist=black_edges, width=2, edge_color='b', arrows=False)
    nx.draw(G, pos=pos, with_labels=True)
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


def Question3(g, path, characters, center_nodes, ancors, dict_characters, colors):
    # # part d
    print('part d:')
    vornoi_partition = vornoi(g, path, characters, center_nodes)
    print('vornoi_partition', vornoi_partition)
    vot_part = translate_voting(nx.MultiDiGraph(g), path, characters, ancors, dict_characters)
    print('vot_part-Directed Weighted', vot_part)
    vot_part = translate_voting(g, path, characters, ancors, dict_characters)
    print('vot_part-UnDirected Weighted', vot_part)
    vot_part = translate_voting(nx.DiGraph(g), path, characters, ancors, dict_characters)
    print('vot_part-Directed UnWeighted', vot_part)
    vot_part = translate_voting(nx.Graph(g), path, characters, ancors, dict_characters)
    print('vot_part-UnDirected UnWeighted', vot_part)
    g2 = createSubGraph(g, path, characters)
    g3 = nx.Graph(g2)

    # Modularity:
    print("Modularity: " + str(nx.algorithms.community.modularity_max.greedy_modularity_communities(g3)))

    # Centrality
    comp = nx.algorithms.community.centrality.girvan_newman(g3)
    for x in comp:
        print("Centrality: " + str(x))
        break

    # Clique Percolation
    print("CliquePercolation: " + str(
        list(nx.algorithms.community.kclique.k_clique_communities(g3, 2))))

    # Vertex Moving:
    print("Vertex Moving: " + str(list(nx.algorithms.community.asyn_fluid.asyn_fluidc(g3, 2))))

    # part g
    print('part g')
    print('printing voting tree result')
    mst_partition(g2, vot_part, colors, center_nodes)
    print('printing vornoi tree result')
    mst_partition(g3, vornoi_partition, colors, center_nodes)
    pass


def results():
    print('movie selected:' + 'batman_begin')
    print()
    g = nx.MultiGraph()
    colors = ['green', 'black', 'blue', 'red']
    path = 'xl_files/batman_begin.xlsx'
    characters = ['BATMAN', 'ALFRED', 'GORDON', 'DUCARD', 'FALCONE', 'FOX', 'RACHEL', 'CRANE', 'EARLE', 'FLASS']
    dict_characters = {0: 'BATMAN', 1: 'ALFRED', 2: 'GORDON', 3: 'DUCARD', 4: 'FALCONE', 5: 'FOX', 6: 'RACHEL',
                       7: 'CRANE', 8: ' EARLE', 9: 'FLASS'}
    center_nodes = ['BATMAN', 'DUCARD', 'CRANE']
    ancors = [0, 3, 7]

    Question3(g, path, characters, center_nodes, ancors, dict_characters, colors)
    print()

    print('movie selected:' + 'thor ragnarok')
    print()
    g = nx.MultiGraph()
    colors = ['green', 'black', 'blue', 'red']
    path = 'xl_files/thor.xlsx'
    characters = ['THOR', 'HELA', 'LOKI', 'VALKYRIE', 'HULK', 'GRANDMASTER', 'SKURGE', 'HEIMDALL', 'SURTUR', 'ODIN']
    dict_characters = {0: 'THOR', 1: 'HELA', 2: 'LOKI', 3: 'VALKYRIE', 4: 'HULK', 5: 'GRANDMASTER', 6: 'SKURGE',
                       7: 'HEIMDALL', 8: 'SURTUR', 9: 'ODIN'}
    center_nodes = ['THOR', 'HELA']
    ancors = [0, 1]


    Question3(g, path, characters, center_nodes, ancors, dict_characters, colors)


results()
