import networkx as nx
import pandas as pd
import Question3_func as Q3

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

# main
g = nx.Graph()
colors = ['green', 'black', 'blue', 'red']

# movie selected:

# for batman_begin-
# path = 'xl_files/batman_begin.xlsx'
# characters = ['BATMAN', 'ALFRED', 'GORDON', 'DUCARD', 'FALCONE', 'FOX', 'RACHEL', 'CRANE', 'EARLE', 'FLASS']
# dict_characters = {0: 'BATMAN', 1: 'ALFRED', 2: 'GORDON', 3: 'DUCARD', 4: 'FALCONE', 5: 'FOX', 6: 'RACHEL',
#                    7: 'CRANE', 8:' EARLE', 9: 'FLASS'}
# center_nodes = {'BATMAN', 'DUCARD', 'FALCONE'}
# ancors = [0, 3, 4]

# for thor ragnarok
path = 'xl_files/thor.xlsx'
characters = ['THOR', 'HELA', 'LOKI', 'VALKYRIE', 'HULK', 'GRANDMASTER', 'SKURGE', 'HEIMDALL', 'SURTUR', 'ODIN']
dict_characters = {0: 'THOR', 1: 'HELA', 2: 'LOKI', 3: 'VALKYRIE', 4: 'HULK', 5: 'GRANDMASTER', 6: 'SKURGE',
                   7: 'HEIMDALL', 8: 'SURTUR', 9: 'ODIN'}
center_nodes = {'THOR', 'HELA', 'HULK'}
ancors = [0, 1, 4]



print("=============================part d=============================")
# Different algorithms for calculating partitioning
actorGraph = createSubGraph(g, path,characters)

# vornoi
print('vornoi_partition: ', Q3.vornoi(g, path, characters, center_nodes))

# voting
print('groups:', nx.voterank(createSubGraph(g, path, characters), 2))
print('voting:',Q3.translate_voting(g, path, characters, ancors, dict_characters))

# Modularity:
print("Modularity: " + str(nx.algorithms.community.modularity_max.greedy_modularity_communities(actorGraph)))

# # Centrality
comp = nx.algorithms.community.centrality.girvan_newman(actorGraph)
for x in comp:
    print("Centrality: " + str(x))
    break
#
# # Clique Percolation
print("CliquePercolation: " + str(list(nx.algorithms.community.kclique.k_clique_communities(actorGraph,2))))
#
# Vertex Moving:
print("Vertex Moving: " + str(list(nx.algorithms.community.asyn_fluid.asyn_fluidc(actorGraph, 2))))
#
# # Kernighan–Lin:
print("Kernighan–Lin algorithm: " + str(list(nx.algorithms.community.kernighan_lin.kernighan_lin_bisection(actorGraph))))

print('part g')
Q3.mst_partition(actorGraph, Q3.vornoi(g, path, characters, center_nodes), colors)