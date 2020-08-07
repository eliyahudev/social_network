import networkx as nx
import pandas as pd
import matplotlib.pyplot as plt


def createGraph(g):
    # get data from xlsx file
    script_df = pd.read_excel('xl_files/script_batman.xlsx')
    speaker = script_df['speaker']

    for i in range(len(speaker)-1):
        g.add_edge(speaker[i], speaker[i+1])
    printGraph(g)

def printGraph(g):
    """vizualization of a graph using mathplotlib library
    input: networkx graph
    output: None"""
    nx.draw(g, with_labels=True)
    plt.show()


# x = df.groupby(['speaker']).count().sort_values('text').to_dict()['text']
createGraph(nx.MultiGraph())