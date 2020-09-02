import matplotlib.pyplot as plt
import networkx as nx
import numpy as np
import pandas as pd

a0, a1, a2, a3 = [], [], [], []
x1, x2, x3, x0 = [], [], [], []
y0, y1, y2, y3 = [], [], [], []


def avrageDigreeCentrality(characters, end_time, start_time):
    df = pd.read_excel(path)
    node_list = df['speaker'].tolist()
    character_degree = len(node_list)
    character_degree_mt = np.zeros((character_degree))
    g = nx.MultiGraph()
    g.add_nodes_from(node_list)

    T = 1

    for i in range(start_time + 1, end_time - 1):
        g.add_edge(node_list[i], node_list[i + 1])
        d = {k: nx.degree_centrality(g)[k] for k in characters}
        x = max(d, key=d.get)
        if str(x).__eq__(characters[0]):
            a0.append(10), x0.append(i), y0.append(start_time)
        elif str(x).__eq__(characters[1]):
            a1.append(10), x1.append(i), y1.append(start_time)
        elif str(x).__eq__(characters[2]):
            a2.append(10), x2.append(i), y2.append(start_time)
        else:
            a3.append(10), x3.append(i), y3.append(start_time)
        # T += 1
    return 1


path = 'xl_files/thor.xlsx'
characters = ['THOR', 'HELA', 'HULK', 'GRANDMASTER']
start = 1
for start in range(1466):
    thor = avrageDigreeCentrality(characters, 1466, start)
    print('\rcreating surface [%.2f%%]' % (start / (1466) * 100), end="")

fig = plt.figure()
ax = fig.add_subplot(111)
ax.scatter(x0, y0,  c='r')
ax.scatter(x1, y1,  c='b')
ax.scatter(x2, y2,  c='g')
ax.scatter(x3, y3,  c='y')
plt.show()
# print('\r')
# print(hela, end='\n\r')
# print(hulk, end='\n\r')
