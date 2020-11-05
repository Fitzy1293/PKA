#!/bin/env python3
from pprint import pprint
import json
import requests
import sys, os
from bs4 import BeautifulSoup

#run ytdl-json

if __name__ == '__main__':
    titles = []
    descriptions = []
    jsonFiles = [file for file in os.listdir('json')]
    for i in jsonFiles:
        if i.startswith(('PKA','Painkiller')):
            words = ''.join(i.split('-')[:-1])
            titleWords = words.split()

            foundInt = False
            for j in titleWords:
                if foundInt:
                    break
                try:
                    epNum = float(j)
                    titles.append((epNum, i))
                    break
                except Exception as e:
                    pass

    sortedTitles = sorted(titles, key=lambda x: (x[0], x[1].lower()))
    sortedTitles.reverse()
    pprint(sortedTitles)
    for i in sortedTitles:

        vidObject = open(f'json/{i[1]}', 'r').read()
        vidDict = json.loads(vidObject)
        description = vidDict['description']
        descriptionFmt = '\t' + '\n\t'.join(description.split('\n'))
        descriptions.append('\t' + '\n\t'.join(description.split('\n')))


    with open('descriptions.txt', 'w+') as f:
        for i in reversed(range(len(sortedTitles))):
            f.write(sortedTitles[i][1])
            f.write('\n' + descriptions[i] + '\n\n')
        f.write('\n')

    foundEps = [i[0] for i in sortedTitles]
    for i in range(1, 516):
        if i not in foundEps:
            print(i)

    print(len(sortedTitles))
