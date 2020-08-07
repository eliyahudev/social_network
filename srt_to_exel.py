import pandas as pd
import re


# & functions & #
def getTextBlock(srt_file):
    """ make an array from srt file
    # input: srt file
    # return: list of strings"""
    f = open(srt_file, 'r')
    x = f.read().split('\n\n')
    f.close()
    return x


def srt_to_df(srt_file):
    """" make lists for the columns of dataFrame
    # input: srt file
    # return: 4 list of strings"""
    start = list()
    end = list()
    text = list()
    speaker = list()
    text_block = getTextBlock(srt_file)
    # separate the text to four column
    for block in text_block:
        if block.__contains__("<b><font"):  # mark speaker with @$
            temp = re.sub('<b><font face="Rockwell" color="#......">', '', block)
            block = re.sub('</font></b>', '@$', temp)

        if block.__contains__("<i>" or "</i>"):  # delete irelevent data
            block = re.sub('<i>|</i>', '', block)

        data = block.split('\n')  # split the string to time (data[1]) and text (all others)
        splt_data1 = re.findall("..:..:..", data[1])  # find the start end the end time
        # get start and end column
        start.append(splt_data1[0])
        end.append(splt_data1[1])
        # get text & speaker column
        text.append(data[2])
        if len(data) > 3:  # if the text is longer then one line
            for i in range(3,len(data)):
                x = text.pop()
                text.append(x + data[i])
        temp2 = text.pop()
        if temp2.__contains__("@$"):
            temp3 = temp2.split('@$')
            if temp2.__contains__("("):
                temp3[0] = re.sub('\(.*\)', '', temp3[0])
            speaker.append(temp3[0])
            text.append(temp3[1])
        else:
            speaker.append('')
            text.append(temp2)
    return start, end, text, speaker


def srt_to_exel(srt_file, exel_file):
    """" make exel file from srt
    # input: srt file
    # return: None """
    start, end, text, speaker = srt_to_df(srt_file)
    df_xl = pd.DataFrame()
    df_xl['start'] = start
    df_xl['end'] = end
    df_xl['text'] = text
    df_xl['speaker'] = speaker
    df_xl.to_excel(exel_file, index=False)


# main
# srt_to_exel('srt_files/Batman.Begins.2005.720p.BluRay.x264. YTS.MX-English.srt', 'xl_files/batman.xlsx')
# srt_to_exel('srt_files/Thor.Ragnarok.2017.WEB-DL.x264-FGT.srt', 'xl_files/thor.xlsx')
