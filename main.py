import Question4
import matplotlib.pyplot as plt
import networkx as nx
import  pandas as pd


def avrageDigreeCentrality(path, character, time):
    df = pd.read_excel(path)
    g = nx.MultiGraph()
    character_degree = dict()
    character_degree[0] = 0
    T = 1
    last = 0
    if not time:
        time = len(df) - 1
    for i in range(0, time):
        g.add_edge(df['speaker'][i], df['speaker'][i+1])
        if not str(df['speaker'][i + 1]).__eq__('nan') and not str(df['speaker'][i]).__eq__('nan'):
            if nx.degree_centrality(g).__contains__(character):
                character_degree[T] = (nx.degree_centrality(g))[character]
            else:
                character_degree[T] = character_degree[T - 1]
        else:
            character_degree[T] = character_degree[T-1]
        T += 1
        # print(nx.degree_centrality(g))
    return character_degree

# inputs
path = 'xl_files/batman_begin.xlsx'
heroes = ['BATMAN', 'DUCARD']
ce = Question4.CeClock(path)
cw = Question4.CwClock(path)
for i in heroes:
    x = avrageDigreeCentrality(path, i, 800) - avrageDigreeCentrality(path, i, 50)
    plt.plot(x.keys(), x.values())
plt.legend(heroes)
plt.show()
