import pandas as pd
# script = 'scripts/batman.txt'
# xl_file = 'xl_files/script_batman.xlsx'


def getTextBlock(script_file):
    """using the dolar sign to separate the text to blocks of speaker and his text
     input: string of text file
     output: list of strings"""
    f = open(script_file, 'r')
    x = f.read().split('$')
    f.close()
    return x


def createColumns(script):
    """get a text an separate it to 2 columns
    input: reference to a text file
    output: two lists"""
    speaker = list()
    text = list()
    data = getTextBlock(script)
    for block in data:
        # reduce cases of empty block of data
        if not len(block):
            continue
        # separate every block to lines
        line = block.split('\n')
        # reduce spaces
        for i in range(len(line)):
            line[i] = line[i].lstrip()
            line[i] = line[i].rstrip()
        # line[0] = speaker and above that is the text
        speaker.append(line[0])
        text.append(line[1])
        # print(line[1])
        for i in range(2,len(line)):
            text.append(text.pop() + line[i])
        return text, speaker


def createExelScript(script, xl_file):
    """create exel file from script
    input: reference to a script, refernce to exel file
    output: None"""
    text, speaker = createColumns(script)
    df_xl = pd.DataFrame()
    df_xl['text'] = text
    df_xl['speaker'] = speaker
    df_xl.to_excel(xl_file, index=False)
