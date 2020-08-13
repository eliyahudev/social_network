import pandas as pd
import matplotlib.pyplot as plt
import math
# 'xl_files/batman_begin.xlsx'


def Convert(lst):
    res_dct = {i : lst[i] for i in range(0, len(lst))}
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
    return ce


def CwClock(path):
    df = pd.read_excel(path)
    text = df['text']
    w = df['text'].str.split().str.len()
    cw = list()
    j = 0
    for i in w:
        # print(i, j, i+j)
        cw.append(i+j)
        if not str(i).__eq__('nan'):
            j += i
        else:
            cw.pop()
            cw.append(j)
    df['cw'] = cw
    df.to_excel(path, index=False)
    return Convert(cw)


def Mdiagram(cw):
    s = len(cw) / cw[len(cw) - 1]
    t = len(cw)
    x = {j: s * i - j for i, j in zip(cw.values(), cw.keys())}
    return x


def MdiagramMinMax(my_dict):
    key_max = max(my_dict.keys(), key=(lambda k: my_dict[k]))
    key_min = min(my_dict.keys(), key=(lambda k: my_dict[k]))
    return (key_max, my_dict[key_max]), (key_min, my_dict[key_min])


def evolving_graph_print(cw):
    plt.plot(cw.keys(),cw.values())
    plt.xlabel(['event'])
    plt.ylabel(['time'])
    plt.legend(['Cw'])
    plt.show()
    plt.clf()


ce = CeClock('xl_files/thor.xlsx')
cw = CwClock('xl_files/thor.xlsx')
evolving_graph_print(ce)
evolving_graph_print(cw)
M = Mdiagram(cw)
evolving_graph_print(M)
print(MdiagramMinMax(M))

# ce = CeClock('xl_files/batman_begin.xlsx')
# cw = CwClock('xl_files/batman_begin.xlsx')
# evolving_graph_print(ce)
# evolving_graph_print(cw)
# M = Mdiagram(cw)
# evolving_graph_print(M)
# print(MdiagramMinMax(M))