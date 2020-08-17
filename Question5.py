
import matplotlib.pyplot as plt
import networkx as nx
import  pandas as pd
from mpl_toolkits import mplot3d
import numpy as np


def avrageDigreeCentrality(node_list, character, end_time, start_time, character_degree_mat):

    if end_time - start_time < 0:
        return avrageDigreeCentrality(node_list, character, start_time, end_time, character_degree_mat) * -1
    last = 0
    g = nx.MultiGraph()
    g.add_nodes_from(node_list)

    T = 1

    for i in range(start_time+1, end_time-1):
        g.add_edge(node_list[i], node_list[i+1])
        if not node_list[i + 1].__eq__('nan') and not node_list[i].__eq__('nan'):
            if node_list[i + 1].__eq__(character) or node_list[i].__eq__(character):
                character_degree_mat[T + start_time] = nx.degree_centrality(g)[character]
                last = character_degree_mat[T + start_time]
            else:
                character_degree_mat[T + start_time] = last
        else:
            character_degree_mat[T + start_time] = last
        T += 1
    # character_degree_mat[T + start_time] = last
    return character_degree_mat


def avrage_degree_graph(path, characters):
    df = pd.read_excel(path)
    node_list = df['speaker'].tolist()
    character_degree = len(node_list)
    for i in range(len(characters)):
        avrage_degree_characters = avrageDigreeCentrality(
            node_list, characters[i], character_degree, 300, np.zeros((character_degree)))
        # print(avrage_degree_characters)
        plt.plot(avrage_degree_characters)
    plt.legend(characters)
    plt.show()
    plt.clf()


def digree_centrality_surface(path, heroes):
    colors = ['b', 'g', 'r', 'm']
    df = pd.read_excel(path)
    node_list = df['speaker'].tolist()
    character_degree = len(node_list)
    matrix = np.zeros((character_degree - 1, character_degree - 1))

    # # Creating figyre
    fig = plt.figure(figsize=(10, 5))
    ax = plt.axes(projection='3d')
    # Creating dataset
    x = np.outer(np.linspace(0, character_degree - 1, character_degree - 1), np.ones(character_degree - 1))
    y = x.copy().T  # transpose
    ln = len(heroes)
    k = 0
    for i in heroes:
        for j in range(character_degree - 1):
            avrageDigreeCentrality(
                node_list, i, character_degree, j, matrix[len(matrix) - 1 - j])
            print('\rcreating surface [%.2f%%]' % (k / (ln * (character_degree - 1)) * 100), end="")
            k += 1
        matrix += np.flip(matrix) * -1
        print(matrix)
    #     surf = ax.plot_surface(x, y, matrix, color=colors.pop())
    #     fig.colorbar(surf, ax=ax, shrink=0.5, aspect=5)
    # #
    # ax.set_title('Surface plot')
    # #
    # # show plot
    # plt.show()


# main
# input
colors = ['b', 'g', 'r', 'm']

# inputs
# path = 'xl_files/batman_begin.xlsx'
# heroes = ['BATMAN']
# heroes = ['FALCONE', 'DUCARD', 'RACHEL', 'GORDON']


path = 'xl_files/thor.xlsx'
heroes = ['HELA', 'HULK']
heroes = ['THOR', 'HELA', 'LOKI', 'VALKYRIE', 'HULK', 'GRANDMASTER', 'SKURGE', 'HEIMDALL', 'SURTUR', 'ODIN']


# avrage_degree_graph(path, heroes)
digree_centrality_surface(path, heroes)
