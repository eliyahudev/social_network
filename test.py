import Question4
import matplotlib.pyplot as plt
import networkx as nx
import  pandas as pd
from mpl_toolkits import mplot3d
import numpy as np


def avrageDigreeCentrality(path, character, end_time, start_time, character_degree, characters):
    if end_time - start_time < 0:
        return avrageDigreeCentrality(path, character, start_time, end_time, character_degree, characters) * -1
    df = pd.read_excel(path)
    g = nx.MultiGraph()
    g.add_nodes_from(characters)
    T = 1 + start_time
    counter = 0
    if not end_time:
        end_time = len(df) - 1
    for i in range(start_time+1, end_time ):
        g.add_edge(df['speaker'][i], df['speaker'][i+1])
        if not str(df['speaker'][i + 1]).__eq__('nan') and not str(df['speaker'][i]).__eq__('nan'):
            if str(df['speaker'][i + 1]).__eq__(character) or str(df['speaker'][i]).__eq__(character):
                counter += 1
                character_degree[T] = counter / len(characters)
            else:
                character_degree[T] = character_degree[T - 1]
        else:
            character_degree[T] = character_degree[T-1]
        T += 1
    return character_degree


# inputs
path = 'xl_files/batman_begin.xlsx'
heroes = ['BATMAN']
# heroes = ['BATMAN', 'DUCARD', 'RACHEL', 'ALFRED']

ce = Question4.CeClock(path)
cw = Question4.CwClock(path)

# Creating dataset
x = np.outer(np.linspace(0, len(ce)-1, len(ce)-1), np.ones(len(ce)-1))
y = x.copy().T  # transpose

# Creating figyre
fig = plt.figure(figsize=(10, 5))
ax = plt.axes(projection='3d')

df = pd.read_excel(path)
# print(df['speaker'].unique())
matrix = np.zeros((len(ce)-1, len(ce)-1))
for j in range(100):
    avrageDigreeCentrality(path, 'DUCARD', j, len(ce)-1, matrix[len(matrix) - 1 - j], df['speaker'].unique())
    print('\rcreating surface [%f%%]' % (j/5.00), end="")
surf = ax.plot_surface(x, y, matrix)
fig.colorbar(surf, ax=ax,
             shrink=0.5, aspect=5)
#
ax.set_title('Surface plot')
#
# show plot
plt.show()


# print(matrix)
# df.to_excel('xl_files/batman_begin_surfaces.xlsx', sheet_name= 'BATMAN', index=False)
