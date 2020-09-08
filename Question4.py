import matplotlib.pyplot as plt
import networkx as nx
import pandas as pd


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

    s = list(ce.values())[-1] / list(cw.values())[-1]
    x = {k: s * i - j for i, j, k in zip(cw.values(), ce.values(), ce.keys())}
    return x


def MdiagramMinMax(my_dict):
    key_max = max(my_dict.keys(), key=(lambda k: my_dict[k]))
    key_min = min(my_dict.keys(), key=(lambda k: my_dict[k]))
    return (key_max, my_dict[key_max]), (key_min, my_dict[key_min])


def evolving_graph_print(cw_list):
    for cw in cw_list:
        plt.plot(list(cw.keys()), list(cw.values()))
    plt.xlabel(['event'])
    plt.ylabel(['time'])
    plt.legend(['Cw'])
    plt.show()
    plt.clf()


def avrage_degree_graph(path, characters):
    for i in range(len(characters)):
        avrage_degree_characters = avrageDigreeCentrality(path, characters[i], None)
        plt.plot(list(avrage_degree_characters.keys()), list(avrage_degree_characters.values()))
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
        plt.plot(list(avrage_degree_M_diagram.keys()), list(avrage_degree_M_diagram.values()))
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
# path = 'xl_files/batman_begin.xlsx'
# second_path = 'xl_files/thor.xlsx'
# # heroes = ['BATMAN', 'DUCARD']
# heroes = ['BATMAN', 'DUCARD', 'RACHEL', 'ALFRED']
# important_words = ['Wayne', 'Gotham', 'stop', 'Master', 'Bruce', 'become', 'Falcone', 'Ra\'s', 'Alfred', 'Rachel',
#                    'Justice', 'crim', 'father', 'company', 'fear', 'Crane', 'people', 'thank', 'Mr', 'you']

path = 'xl_files/thor.xlsx'
heroes = ['THOR', 'HELA']
important_words = ['Asgard', 'Hulk', 'Thor', 'place', 'people', 'Odin', 'stop', 'Ragnarok',
                   'Thunder', 'hammer', 'Hela', 'God', 'death', 'time', 'think', 'kind', 'past', 'thank', 'honored',
                   'you']

second_path = 'xl_files/batman_begin.xlsx'
second_heroes = ['BATMAN', 'DUCARD', 'RACHEL', 'ALFRED']
second_important_words = ['Wayne', 'Gotham', 'stop', 'Master', 'Bruce', 'become', 'Falcone', 'Ra\'s', 'Alfred', 'Rachel',
                   'Justice', 'crim', 'father', 'company', 'fear', 'Crane', 'people', 'thank', 'Mr', 'you']


def Question4(path, heroes, important_words):
    # answers
    print('part a,b')
    print('creating clocks for thor')
    ce = CeClock(path)
    cw = CwClock(path)
    cl = ClClock(path, important_words)

    print('creating clocks for batman')
    second_ce = CeClock(second_path)
    second_cw = CwClock(second_path)
    second_cl = ClClock(second_path, second_important_words)

    print('pard c')
    print('print ce, cw for thor movie')
    evolving_graph_print([ce])
    evolving_graph_print([normalizeClock(ce)])
    evolving_graph_print([cw])
    evolving_graph_print([normalizeClock(cw)])

    print('print ce, cw for batman movie')
    evolving_graph_print([second_ce])
    evolving_graph_print([normalizeClock(second_ce)])
    evolving_graph_print([second_cw])
    evolving_graph_print([normalizeClock(second_cw)])

    print('plot Mdiagram(ce, cw) for thor movie')
    M = Mdiagram(cw, ce)
    M2 = Mdiagram(normalizeClock(cw), normalizeClock(ce))
    evolving_graph_print([cw, ce])
    evolving_graph_print([M])
    evolving_graph_print([M2])
    print('find min and max for thor')
    print(MdiagramMinMax(M))

    print('plot Mdiagram(ce, cw) for batman movie')
    M3 = Mdiagram(second_cw, second_ce)
    M4 = Mdiagram(normalizeClock(second_cw), normalizeClock(second_ce))
    evolving_graph_print([M3])
    evolving_graph_print([M4])
    print('find min and max for batman')
    print(MdiagramMinMax(M3))

    print('comparence between thor and batman Mdiagram')
    evolving_graph_print([M4, M2])

    print('part d')
    print('avrage degree graph for thor:')
    avrage_degree_graph(path, heroes)
    print('avrage degree graph for batman:')
    avrage_degree_graph(second_path, second_heroes)

    print('part e')
    print('avrage degree M diagram graph for thor:')
    avrageDegreeMDiagram(path, heroes, ce)
    print('avrage degree M diagram graph for batman:')
    avrageDegreeMDiagram(second_path, second_heroes, second_ce)

    print('part f')
    print('print cl clock for thor')
    evolving_graph_print([cl])
    print('print cl clock for batman')
    evolving_graph_print([second_cl])

    print('Part g')
    print('print Mdiagram(cl,ce) clock for thor')
    evolving_graph_print([Mdiagram(cl, ce)])
    print('print Mdiagram(cl,ce) clock for batman')
    evolving_graph_print([Mdiagram(second_cl, second_ce)])

    print('part h')
    print('comparence between thor and batman cw clock')
    evolving_graph_print([normalizeClock(second_cw), normalizeClock(cw)])
    print('Mdiagram with thor and batman cw clock')
    # evolving_graph_print([Mdiagram(normalizeClock(second_cw), normalizeClock(cw))])


    M5 = {k: i - j for i, j, k in zip(M.values(), M3.values(), M3.keys())}
    evolving_graph_print([M5])

Question4(path, heroes, important_words)
