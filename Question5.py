import Question4 as Q4
import matplotlib.pyplot as plt
import networkx as nx
import  pandas as pd
from mpl_toolkits import mplot3d
import numpy as np


def avrageDigreeCentrality(path, character, end_time, start_time, character_degree, characters):

    if end_time - start_time < 0:
        return avrageDigreeCentrality(path, character, start_time, end_time, character_degree, characters) * -1
    last = 0
    df = pd.read_excel(path)
    g = nx.MultiGraph()
    g.add_nodes_from(characters)
    T = 1 + start_time

    if not end_time:
        end_time = len(df) - 1
    for i in range(start_time+1, end_time ):
        g.add_edge(df['speaker'][i], df['speaker'][i+1])
        if not str(df['speaker'][i + 1]).__eq__('nan') and not str(df['speaker'][i]).__eq__('nan'):
            if str(df['speaker'][i + 1]).__eq__(character) or str(df['speaker'][i]).__eq__(character):
                if nx.degree(g, character):
                    character_degree[T] = nx.degree(g, character) / (2 * T)
                    last = nx.degree(g, character)
                else:
                    character_degree[T] = last / (2 * T)
            else:
                character_degree[T] = last / (2 * T)
        T += 1
    return character_degree


def avrage_degree_graph(path, characters):
    for i in range(len(characters)):
        avrage_degree_characters = avrageDigreeCentrality(path, characters[i], 361, 337, np.zeros((361 - 337)), characters)
        plt.plot(avrage_degree_characters)
    plt.legend(characters)
    plt.show()
    plt.clf()


# inputs
path = 'xl_files/batman_begin.xlsx'
# heroes = ['BATMAN']
heroes = ['BATMAN', 'DUCARD', 'RACHEL', 'GORDON']
comd_colors = ['hot', 'Dark2', 'Blues', 'gray']

ce = Q4.CeClock(path)
cw = Q4.CwClock(path)

avrage_degree_graph(path, heroes)



# # Creating dataset
# x = np.outer(np.linspace(0, len(ce)-1, len(ce)-1), np.ones(len(ce)-1))
# y = x.copy().T  # transpose
#
# # Creating figyre
# fig = plt.figure(figsize=(10, 5))
# ax = plt.axes(projection='3d')
#
# df = pd.read_excel(path)
# # print(df['speaker'].unique())
# # matrix = np.zeros(5)
# matrix = np.zeros((len(ce)-1, len(ce)-1))
# for i in heroes:
#     for j in range(len(ce)-1):
#         avrageDigreeCentrality(path, i, j, len(ce)-1, matrix[len(matrix) - 1 - j], df['speaker'].unique())
#         print('\rcreating surface [%f%%]' % (j/(len(ce)-1)*100), end="")
#     my_cmap = plt.get_cmap(comd_colors.pop())
#     surf = ax.plot_surface(x, y, matrix, cmap = my_cmap)
#     fig.colorbar(surf, ax=ax, shrink=0.5, aspect=5)
# #
# ax.set_title('Surface plot')
# #
# # show plot
# plt.show()
# #
# # df1 = pd.DataFrame(data=matrix.tolist())
# # # print(df)
# # df1.to_excel('xl_files/batman_begin_surface.xlsx', 'BAT', engine='openpyxl', index=False)
#
#
#
# # print
# # df.to n_surfaces.xlsx', sheet_name= 'BATMAN', index=False)
