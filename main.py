import graph_creator
import networkx as nx


def createSubGraph(graph, path, characters_list):
    g = graph_creator.thorCreatGraph(graph, path)
    g2 = nx.MultiGraph(nx.subgraph(g, characters_list))
    return g2


g2 = createSubGraph(nx.MultiGraph(),'xl_files/script_thor.xlsx', ['THOR', 'HELA', 'LOKI', 'VALKYRIE', 'HULK'
     , 'GRANDMASTER', 'SKURGE', 'HEIMDALL', 'SURTUR', 'ODIN'])

graph_creator.printGraph(g2)

g3 = createSubGraph(nx.MultiGraph(),'xl_files/script_batman.xlsx', ['BATMAN', 'RA\'S AL GHUL', 'ALFRED',
                                                                      'GORDON', 'FALCONE', 'FOX', 'RACHEL',
                                                                      'CRANE', 'EARLE', 'FLASS'])
graph_creator.printGraph(g3)