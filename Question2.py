import graph_creator
import networkx as nx
# main
path1 = 'xl_files/thor.xlsx'
path2 = 'xl_files/batman_begin.xlsx'
print('Question 2:')
print('part a,b')
print()
g = graph_creator.thorCreatGraph(nx.MultiGraph(), path1)
g2 = graph_creator.thorCreatGraph(nx.MultiGraph(), path2)
graph_creator.printGraph(g)  # print AB graph
graph_creator.printGraph(g2)
print("Thor ragnarok characters: ", g.nodes)  # show the characters
print("Batman begin characters:", g2.nodes)
print()
print()

print('part c')
print('#nodes(left) & #edges(right) for "Thor ragnarok": ', graph_creator.count_edges_and_nodes(g))  # print #nodes(left) & #edges(right)
print('#nodes(left) & #edges(right) for "Batman begin": ', graph_creator.count_edges_and_nodes(g2))  # print #nodes(left) & #edges(right)
print()
print()
print('part d')
graph_creator.get_centrality('Thor ragnarok_', path1)
graph_creator.get_centrality('Batman begin_', path2)
