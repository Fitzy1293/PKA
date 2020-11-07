#!/bin/env python3
from pprint import pprint
import json
import requests
import sys, os
from bs4 import BeautifulSoup
import sys

def handleEpFromTitle(title):
    missingEps = (101, 169, 306, 350, 355) # Deleted.

    if title.startswith('10 Year Anniversary'):
        return (488, title)
    elif title.startswith('Painkiller Already 169'): # Miss-titled. 169 is missing.
        return (168, 'Painkiller Already 169-NRrm-MomDD8.info.json')
    elif title.startswith('Painkiller Already160'):
        return (160, 'Painkiller Already160 w_ Joe Lauzon-3yWkj9Q4J-U.info.json')
    elif title.startswith('Painkiller Already 163'):
        return (163, 'Painkiller Already 163-CgNKKH-dC7c.info.json')
    elif title.startswith('PKA Road to Black Ops 2'):
        return (111, 'PKA Road to Black Ops 2 - Painkiller Already 111-Dh9BgaVn6ds.info.json')
    elif title.startswith('Painkiller Already 99'):
        return (99, 'Painkiller Already 99w_Ons1augh7 and Izedneck-M4PDCvH_fyE.info.json')
    elif title.startswith('Painkiller Already Episode 56'):
        return (56, 'Painkiller Already Episode 56.5 w_KimmyJ, ThatCoolBlackGuy-sNA248y7keE.info.json')


    else:
         return None

def main():
        titles = []
        descriptions = []
        pkaFiles = []
        links = []


        for i in os.listdir('json'):
            dashCt = i.count('-') #One fname had two so need to count for slice.

            titleBehavior = handleEpFromTitle(i)
            if titleBehavior is not None:
                pkaFiles.append(titleBehavior)
                continue

            if i.startswith(('PKA','Painkiller')):
                words = ''.join(i.split('-')[:-dashCt])
                titleWords = words.split()

                foundInt = False
                for j in titleWords:
                    if foundInt:
                        break
                    try:
                        if j.startswith('#'):
                            pkaFiles.append(float(j[1:]), i)

                        else:
                            pkaFiles.append((float(j), i))
                        break
                    except Exception as e:
                        pass

        sortedTitles = sorted(pkaFiles, key=lambda x: (x[0], x[1].lower()), reverse=True)
        for i in sortedTitles:

            vidObject = open(f'json/{i[1]}', 'r').read()
            vidDict = json.loads(vidObject)
            description = vidDict['description']
            descriptionLines = description.split('\n')

            timestamps = []
            timeLineStarted = False
            for line in descriptionLines:

                if line.strip()[0:2] == '0:' or timeLineStarted:
                    timeLineStarted = True

                    timestamps.append(line)

            allTimestamps = '\t' + '\n\t'.join(timestamps)
            descriptions.append(allTimestamps)
            titles.append(vidDict['fulltitle'])
            links.append(f'https://www.youtube.com/watch?v={vidDict["id"]}')


        with open('timelines_copy.txt', 'w+') as f:
            for i in range(len(sortedTitles)):
                f.write(titles[i])
                f.write('\n' + links[i])
                f.write('\n' + descriptions[i] + '\n\n')
            f.write('\n')

        foundEps = [i[0] for i in sortedTitles]
        missingTimelines = []
        for i in range(1, 516):
            if i not in foundEps:
                missingTimelines.append(i)

        pprint(f'missing:\n{missingTimelines}')
        print(len(sortedTitles))

if __name__ == '__main__':

    main()
