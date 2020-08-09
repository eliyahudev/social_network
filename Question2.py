import graph_creator
import networkx as nx
# main
print('Question 2:')
# error test
print('part a,b')
print()
g = graph_creator.thorCreatGraph(nx.MultiGraph(), 'xl_files/script_thor.xlsx')
g2 = graph_creator.batmaCreateGraph(nx.MultiGraph(), 'xl_files/script_batman.xlsx')
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
# dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddf
print('part d')
graph_creator.get_centrality('Thor ragnarok', 'xl_files/script_thor.xlsx')
graph_creator.get_centrality('Batman begin:', 'xl_files/script_batman.xlsx')
