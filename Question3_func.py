import graph_creator
import networkx as nx
import random


def createSubGraph(graph, path, characters_list):
    g = graph_creator.thorCreatGraph(graph, path)
    g2 = nx.MultiGraph(nx.subgraph(g, characters_list))
    return g2


#
# graph_creator.printGraph(g2)
#
# g3 = createSubGraph()
# graph_creator.printGraph(g3)
# center_nodes1 = {'THOR', 'HELA', 'GRANDMASTER'}
# cells1 = nx.voronoi_cells(g2, center_nodes1)
# print(cells1)
#
# center_nodes2 = {'BATMAN', 'CRANE', 'RA\'S AL GHUL'}
# cells2 = nx.voronoi_cells(g3, center_nodes2)
# print(cells2)
#
#
# print(nx.algorithms.voterank(g3, 3))

# adj_met = nx.adjacency_matrix(g2)
# print(adj_met)


def vornoi_calculate_thor(g, path, characters_list):
     g2 = createSubGraph(g, path, characters_list)
     new_g = nx.MultiGraph();
     for i in g2.nodes:
          while g2.get_edge_data(i, i):
               g2.remove_edge(i, i)
          for i in g2.nodes:
               for j in g2.nodes:
                    if g2.number_of_edges(i,j):
                         new_g.add_edge(i,j, 1/g2.number_of_edges(i,j))
          # print(new_g.edges)
     i = (dict(nx.algorithms.shortest_paths.all_pairs_dijkstra(new_g))['HELA'])
     j = (dict(nx.algorithms.shortest_paths.all_pairs_dijkstra(new_g))['THOR'])
     hela = list()
     thor = list()
     for k in new_g.nodes:
          if i[0][k] > j[0][k]:
               thor.append(k)
          elif i[0][k] < j[0][k]:
               hela.append(k)
          else:
               r = random.randint(0,1)
               thor.append(k) if r == 1 else hela.append(k)
     print(hela, thor)
          # print(i)


def vornoi_calculate_batman(g, path, characters_list):
     g2 = createSubGraph(g, path, characters_list)
     new_g = nx.MultiGraph();
     for i in g2.nodes:
          while g2.get_edge_data(i, i):
               g2.remove_edge(i, i)
          for i in g2.nodes:
               for j in g2.nodes:
                    if g2.number_of_edges(i,j):
                         new_g.add_edge(i,j, 1/g2.number_of_edges(i,j))
          # print(new_g.edges)

     i = (dict(nx.algorithms.shortest_paths.all_pairs_dijkstra(new_g))['BATMAN'])
     j = (dict(nx.algorithms.shortest_paths.all_pairs_dijkstra(new_g))['RA\'S AL GHUL'])
     batman = list()
     rachel = list()
     for k in new_g.nodes:
          if i[0][k] > j[0][k]:
               batman.append(k)
          elif i[0][k] < j[0][k]:
               rachel.append(k)
          else:
               r = random.randint(0,1)
               batman.append(k) if r == 1 else rachel.append(k)
     print(batman, rachel)
          # print(i)



vornoi_calculate_thor(nx.MultiGraph(), 'xl_files/script_thor.xlsx',
                         ['THOR', 'HELA', 'LOKI', 'VALKYRIE', 'HULK',
                          'GRANDMASTER', 'SKURGE', 'HEIMDALL', 'SURTUR', 'ODIN'])
vornoi_calculate_batman(nx.MultiGraph(), 'xl_files/script_batman.xlsx',
                    ['BATMAN', 'RA\'S AL GHUL', 'ALFRED', 'GORDON', 'FALCONE',
                     'FOX', 'RACHEL', 'CRANE', 'EARLE', 'FLASS'])