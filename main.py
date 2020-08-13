"test"
import pandas as pd
import re
def manipulate_page():
    df_thor = pd.read_excel('xl_files/thor.xlsx')
    df_script_thor = pd.read_excel('xl_files/script_thor.xlsx')
    x=0
    for i in df_thor['text']:
        x+=1
        for j,z in zip(df_script_thor['text'], df_script_thor['speaker']):
            # if (str(j).capitalize()).__contains__(str(i).capitalize()) and  str(df_thor['speaker'][x]).__contains__('nan'):
            if re.search(str(i).capitalize(), str(j).capitalize()) and str(df_thor['speaker'][x]).__contains__('nan'):
                df_thor['speaker'][x] = z
                print(j,"; ", i, "; ", z,x)

    for i in df_thor['speaker']:
        print(i)
    df_thor.to_excel('xl_files/test_xl.xlsx', index=False)


def manipulate_page2():
    df_thor = pd.read_excel('xl_files/batman1.xlsx')
    df_script_thor = pd.read_excel('xl_files/script_batman.xlsx')
    x=0
    for i in df_thor['text']:
        for j,z in zip(df_script_thor['text'], df_script_thor['speaker']):

            if (str(i).capitalize()).__contains__(str(j).capitalize()) and  str(df_thor['speaker'][x]).__contains__('nan'):
                # if re.search(str(j).capitalize(), str(i).capitalize()) and\
                #         str(j).__contains__() and str(df_thor['speaker'][x]).__contains__('nan'):
                df_thor['speaker'][x] = z
                print(j,"; ", i, "; ", z,x)
        x+=1
    # test
    for i in df_thor['speaker']:
        print(i)
    df_thor.to_excel('xl_files/test_xl1.xlsx', index=False)
manipulate_page2()
"ttttttttttttttttttttttttteeeeeeeeeeeeeeeeeesssssssssssssssseeeeeeeeeettttttttt"