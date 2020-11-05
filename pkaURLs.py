#!/bin/env python3
from pprint import pprint
import json
import requests
import sys, os
from bs4 import BeautifulSoup



if __name__ == '__main__':
    titles = []
    descriptions = []

    for file in os.listdir('json'):

        vidObject = open(f'json/{file}', 'r').read()
        vidDict = json.loads(vidObject)
        description = vidDict['description']
        title = vidDict['fulltitle']

        descriptionFmt = '\t' + '\n\t'.join(description.split('\n'))
        descriptions.append('\t' + '\n\t'.join(description.split('\n')))
        titles.append('\n'.join(title.split('\n')))
    with open('descriptions.txt', 'w+') as f:
        for i in reversed(range(len(descriptions))):
            f.write(titles[i])
            f.write('\n' + descriptions[i] + '\n\n')
        f.write('\n')
