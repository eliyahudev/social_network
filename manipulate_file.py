import re
def getTextBlock(srt_file):
    f = open(srt_file, 'r+')
    z = f.read()
    # re.sub(' \(V.O.\)|\(Thor looks back\)| \(O.S.\)|\(MORE\)|\(GIGGLES to himself\)|\(awaiting an answer\)|\(notices:\)|\(then:\)|\(beat\)|\(refocuses\)|\(to Loki\)|(to Valkyrie)','', z)
    x = z.split('\n')
    f.close()
    return x


f = open('scripts/batman.txt', 'w+')
y = list
x = getTextBlock('xml_script/BATMAN_BEGINS.txt')

for i in x:

    if i.__contains__('             ') and not i.__contains__('INT.')\
            and not i.__contains__('EXT.') and not i.__contains__('INT.')\
            and not i.__contains__('DRAFT') and not i.__contains__('OMITTED')\
            and not i.__contains__("CONT'D") and not re.search('(0+|1+|2+|3+|4+|5+|6+|7+|8+|9+)\.', i)\
            and not i.__contains__("CUT TO:") and not i.__contains__("DISSOLVE TO:"):
        if re.search('\(.*\)', i):
            i = re.sub('\(.*\)', '', i)
        if i.__contains__('                               ') :
            i = '$' + i
            # print(i)
        f.write(i + '\n')
f.close()
print('done')