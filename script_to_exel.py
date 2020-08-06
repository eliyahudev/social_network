import pandas as pd

""" tranport """
def getTextBlock(script_file):
    f = open(script_file, 'r')
    x = f.read().split('$')
    f.close()
    return x


speaker = list()
text = list()
data = getTextBlock('scripts/batman.txt')
for block in data:
    if not len(block):
        continue
    line = block.split('\n')
    for i in range(len(line)):
        line[i] = line[i].lstrip()
        line[i] = line[i].rstrip()
        print(line[i])
    speaker.append(line[0])
    text.append(line[1])
    # print(line[1])
    for i in range(2,len(line)):
        text.append(text.pop() + line[i])
df_xl = pd.DataFrame()
df_xl['text'] = text
df_xl['speaker'] = speaker
df_xl.to_excel('xl_files/script_batman.xlsx', index=False)
