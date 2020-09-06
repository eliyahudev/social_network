import matplotlib.pyplot as plt
import networkx as nx
import pandas as pd

a0, a1, a2, a3 = [], [], [], []
x1, x2, x3, x0 = [], [], [], []
y0, y1, y2, y3 = [], [], [], []

a0n, a1n, a2n, a3n = [], [], [], []
x1n, x2n, x3n, x0n = [], [], [], []
y0n, y1n, y2n, y3n = [], [], [], []


def avrageDigreeCentrality(g, characters, end_time, start_time):
    for i in range(start_time + 1, end_time - 1):
        g.add_edge(node_list[i], node_list[i + 1])
        deg_cent = nx.degree_centrality(g)
        d = {k: deg_cent[k] for k in characters}
        x = max(d, key=d.get)
        z = min(d, key=d.get)

        # get the highest
        if str(x).__eq__(characters[0]):
            x0.append(i), y0.append(start_time)
        elif str(x).__eq__(characters[1]):
            x1.append(i), y1.append(start_time)
        elif str(x).__eq__(characters[2]):
            x2.append(i), y2.append(start_time)
        else:
            x3.append(i), y3.append(start_time)

        # get the lowest
        if str(z).__eq__(characters[0]):
            x0n.append(start_time), y0n.append(i)
        elif str(z).__eq__(characters[1]):
            x1n.append(start_time), y1n.append(i)
        elif str(z).__eq__(characters[2]):
            x2n.append(start_time), y2n.append(i)
        else:
            x3n.append(start_time), y3n.append(i)


path = 'xl_files/thor.xlsx'
movie_name = 'THOR RAGNAROCK'
characters = ['LOKI', 'HELA', 'HULK', 'GRANDMASTER']
movie_length = 1560

# path = 'xl_files/batman_begin.xlsx'
# movie_name = 'BATMAN BEGIN'
# characters = ['BATMAN', 'DUCARD', 'RACHEL', 'FALCONE']
# movie_length = 1466

df = pd.read_excel(path)
node_list = df['speaker'].tolist()

for start in range(movie_length):
    g = nx.MultiGraph()
    g.add_nodes_from(node_list)
    avrageDigreeCentrality(g, characters, movie_length, start)
    print('\rcreating surface [%.2f%%]' % (start / (movie_length) * 100), end="")

# plot degree centrality surface
fig = plt.figure(movie_name)
ax = fig.add_subplot(111)

# draw the highes value
ax.scatter(x0, y0, c='r')
ax.scatter(x1, y1, c='b')
ax.scatter(x2, y2, c='g')
ax.scatter(x3, y3, c='y')

# draw the lowest value
ax.scatter(x0n, y0n, c='r')
ax.scatter(x1n, y1n, c='b')
ax.scatter(x2n, y2n, c='g')
ax.scatter(x3n, y3n, c='y')

# show
# plt.legend(characters)
plt. show()
