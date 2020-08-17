import matplotlib.pyplot as plt
import networkx as nx
import pandas as pd


# TODO change characters ':' in batman begin xl


def avrageDigreeCentrality(path, character, time):
    df = pd.read_excel(path)
    g = nx.MultiGraph()
    g.add_nodes_from(df['speaker'].unique().tolist())
    character_degree = dict()
    character_degree[0] = 0
    T = 1
    last = 0
    if not time:
        time = len(df) - 1
    for i in range(0, time):
        g.add_edge(df['speaker'][i], df['speaker'][i + 1])
        if not str(df['speaker'][i + 1]).__eq__('nan') and not str(df['speaker'][i]).__eq__('nan'):
            if nx.degree(g, character):
                character_degree[T] = nx.degree(g, character) / (2 * T)
                last = nx.degree(g, character)
            else:
                character_degree[T] = last / (2 * T)
        else:
            character_degree[T] = last / (2 * T)
        T += 1
    return character_degree


def Convert(lst):
    res_dct = {i: lst[i] for i in range(0, len(lst))}
    return res_dct


def create_ce_clock(path):
    df = pd.read_excel(path)
    col = df['speaker']
    Ce = 0
    row_num = 0
    for row in col:
        if not str(row).__contains__('nan'):
            df['Ce'][row_num] = Ce
            Ce += 1
        row_num += 1
    df.to_excel(path, index=False)


def normalizeClock(clock):
    new_clock = {i / (len(clock) - 1): j / clock[len(clock) - 1] for i, j in zip(clock.keys(), clock.values())}
    return new_clock


def CeClock(path):
    df = pd.read_excel(path)
    actor = df['speaker']
    counter = 0
    y = 0
    ce = dict()
    for i in actor:
        counter += 1
        ce[y] = counter
        y += 1
    df['ce'] = ce
    df.to_excel(path, index=False)
    return ce


def CwClock(path):
    df = pd.read_excel(path)
    text = df['text']
    w = df['text'].str.split().str.len()
    cw = list()
    j = 0
    for i in w:
        # print(i, j, i+j)
        cw.append(i + j)
        if not str(i).__eq__('nan'):
            j += i
        else:
            cw.pop()
            cw.append(j)
    df['cw'] = cw
    df.to_excel(path, index=False)
    return Convert(cw)


def ClClock(path, important_words):
    ls = pd.read_excel(path)
    df = pd.DataFrame(ls['text'].str.split(), columns=['text'])
    cl = dict()
    # initial condition for cl[0]
    if df['text'][0] in important_words:
        cl[0] = 1
    else:
        cl[0] = 0
    T = 1
    for i in df['text']:
        cl[T] = cl[T - 1]  # the is growing as a function of the for amount
        if not str(i).__eq__('nan'):  # check if the row is not empty
            for j in i:
                if j in important_words:  # count only word that belong to the important words chosen
                    cl[T] += 1
        T += 1
    return cl


def Mdiagram(cw, ce):
    len_cw = len(cw)
    len_ce = len(ce)
    # hefresh = len_cw - len_ce
    # if hefresh != 0:
    #     if hefresh > 0:
    #         for i in range(hefresh):
    #             cw.pop(random.randint(0,(len_cw - 1))/(len_cw - 1))
    #     else:
    #         for i in range(-hefresh):
    #             cw.pop(random.randint(0, (len_ce - 1))/(len_ce - 1))
    s = list(ce.values())[-1] / list(cw.values())[-1]
    x = {k: s * i - j for i, j, k in zip(cw.values(), ce.values(), ce.keys())}
    return x


# TODO delite the function
# def NormalizeMDiagram(cw, ce):
#     s = ce[len(ce) - 1] / cw[len(cw) - 1]
#     x = {k / len(ce): s * i - j for i, j, k in zip(cw.values(), ce.values(), ce.keys())}
#     return x


def MdiagramMinMax(my_dict):
    key_max = max(my_dict.keys(), key=(lambda k: my_dict[k]))
    key_min = min(my_dict.keys(), key=(lambda k: my_dict[k]))
    return (key_max, my_dict[key_max]), (key_min, my_dict[key_min])


def evolving_graph_print(cw_list):
    for cw in cw_list:
        plt.plot(cw.keys(), cw.values())
    plt.xlabel(['event'])
    plt.ylabel(['time'])
    plt.legend(['Cw'])
    plt.show()
    plt.clf()


def avrage_degree_graph(path, characters):
    for i in range(len(characters)):
        avrage_degree_characters = avrageDigreeCentrality(path, characters[i], None)
        plt.plot(avrage_degree_characters.keys(), avrage_degree_characters.values())
    plt.legend(characters)
    plt.show()
    plt.clf()


def avrageDegreeMDiagram(path, characters, ce):
    """vizualize M diagram for multiple characters at
       the same plate,
       parameters:
       ----------
       path: reference to xl file
       characters: list of characters to print
       ce: clock to compere to
       return:
       -------
       None
       """
    for i in range(len(characters)):
        avrage_degree_M_diagram = Mdiagram(avrageDigreeCentrality(path, characters[i], None), ce)
        plt.plot(avrage_degree_M_diagram.keys(), avrage_degree_M_diagram.values())
    plt.legend(characters)
    plt.show()


def WordsCounter(path):
    """count words appearance in the text
    input: reference to exel file
    output: None"""
    ls = pd.read_excel(path)
    # l = map()
    df = pd.DataFrame(ls['text'].str.split(), columns=['text'])
    x = dict()
    for i in df['text']:
        if not str(i).__eq__('nan'):
            for j in i:
                if x.__contains__(j):
                    x[j] += 1
                else:
                    x[j] = 1
    z = sorted(x.items(), key=lambda x: x[1], reverse=True)
    for i in range(len(z)):
        print(z[10 * i: 10 * (i + 1)])


# inputs
path = 'xl_files/batman_begin.xlsx'
second_path = 'xl_files/thor.xlsx'
# heroes = ['BATMAN', 'DUCARD']
heroes = ['BATMAN', 'DUCARD', 'RACHEL', 'ALFRED']

# heroes = ['THOR', 'HELA']
# important_words = ['Asgard','Hulk','Thor','place','people','Odin','stop','Ragnarok',
#                    'Thunder','hammer','Hela','God','death','time','think','kind','past','thank','honored','you']
important_words = ['Wayne', 'Gotham', 'stop', 'Master', 'Bruce', 'become', 'Falcone', 'Ra\'s', 'Alfred', 'Rachel',
                   'Justice', 'crim', 'father', 'company', 'fear', 'Crane', 'people', 'thank', 'Mr', 'you']
# answers
# part a,b
ce = CeClock(path)
# second_ce = CeClock(second_path)
cw = CwClock(path)
cl = ClClock(path, important_words)
# second_cw = CwClock(second_path)

# pard c
# evolving_graph_print([ce])
# evolving_graph_print([normalizeClock(ce)])
# evolving_graph_print([cw])
# evolving_graph_print([normalizeClock(cw)])

# M = Mdiagram(cw, ce)
# M2 = Mdiagram(normalizeClock(cw), normalizeClock(ce))
# evolving_graph_print([cw, ce])
# evolving_graph_print([M])
# evolving_graph_print([M2])

# print(MdiagramMinMax(M))
# ce = CeClock(path)
# cw = CwClock(path)
# evolving_graph_print([ce])
# evolving_graph_print([cw])


# M = Mdiagram(cw, ce)
# M2 = Mdiagram(second_cw, second_ce)
# evolving_graph_print([M,M2])
# print(MdiagramMinMax(M))

# part d
# avrage_degree_graph(path, heroes)

# part e
# avrageDegreeMDiagram(path, heroes, ce)

# part f
# WordsCounter(path)
# evolving_graph_print(cl)

# part g
# print('Part g')
# evolving_graph_print([Mdiagram(cl, ce)])

# part h
# evolving_graph_print([normalizeClock(second_cw), normalizeClock(cw)])
# evolving_graph_print([Mdiagram(normalizeClock(second_cw), normalizeClock(cw))])

# M = NormalizeMDiagram(cw, ce)
# M2 = NormalizeMDiagram(second_cw, second_ce)
# evolving_graph_print([M,M2])
# M3 = {k: i - j for i, j, k in zip(M.values(), M2.values(), M2.keys())}
# evolving_graph_print([M3])
# evolving_graph_print([Mdiagram(cw, second_cw)])

# M = dict()
# T = 0
# for i in df['text']:
#     if not str(i).__eq__('nan'):
#         while T < min(len(cl),len(ce)):
#             M[T] = cl[T] - ce[T]
#             T += 1
#
# evolving_graph_print([M])
