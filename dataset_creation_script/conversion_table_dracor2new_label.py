# conversion table from the 87 most common stage directions types in FreDraCor 
# into the 13 classes typology.

import re
dracor_types = [['entrance', 'entrée'],
            ['exit', 'escape'],
            ["location", "decor", 'décor'],
            ['narration', 'meteo', 'noise'],
            ["toward"],
            ["aparte", 'alone'],
            ["together", "call", "interrupt", 'loud', 'low', 'laugh', 'silence', 'quiet', 'cry', 'shout', 'nervous', 'ironic', 'anger', 'serious', 'happy', 'hesitate', 'enthousiasm', 'emotion', 'emphasis', 'friendly', 'grimace', 'feeling', 'furious', 'continue', 'sing', 'repeat'],
            ['kiss', 'touch', 'help', 'pull', 'push' ],
            ['kill', 'fight', 'hit', 'suicide', 'threat'],
            ['action', 'watch', 'show', 'paint', 'pray', 'jump', 'read', 'kneel', 'fall', 'knock', 'write', 'drink', 'search', 'open', 'eat', 'sleep', 'stand', 'sit', 'move', 'listen', 'ring'],
            ['closer',  'away', 'walk', 'follow', 'back'],
            ['costume', 'throw', 'tear', 'get', 'give', 'dress', 'drop', 'close'],
            ['music', 'title', 'ttitle', 'bis' ]]
new_types = ['entrance', 'exit', 'setting','narration', 'toward', 'aparte', 'delivery', 'interaction', 'aggression', 'action', 'movement', 'object', 'music']


def write():
    # écriture du csv contenant l'etiquette pour la classification :
    with open("./data/stgdir_labelDraCor_no-mixed-type.csv", "r", encoding="utf8") as f,\
        open("./data/stgdir_labelGeneric.csv", "a", encoding="utf8") as new,\
        open("./data/stgdir_labelDraCor.csv", "a", encoding="utf8") as old:
        new.write('description|labelGeneric\n')
        old.write('description|labelDraCor\n')
        # going through the file without "mixed" stage directions (e.g. "fight/exit")
        for line in f:
            l = line.rstrip()
            try :
                descr, labelDraCor = l.split("|")
            finally : 
                # looking for a match in the original types
                for x in range(len(dracor_types)):
                    if labelDraCor.lower() in dracor_types[x]:
                        # creating a temporary new label
                        both_labels = f"{labelDraCor.lower()}|{new_types[x]}"
                if re.search(r"\|", labelDraCor):
                    new.write(descr+ "|" + both_labels.split("|")[1] +'\n')
                    old.write(descr+ '|' + both_labels.split('|')[0] + '\n')
