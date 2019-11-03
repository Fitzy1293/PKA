import requests
import os
from pprint import pprint
import json
import csv

#painkilleralready.info didn't have all timelines available.
#Youtube has an api but didn't feel like learning it.
def main(url):

    with open(url, 'r') as f:
        episodes = json.load(f)['episodes']

    with open('Timeline.txt','w+') as f:
        for episode in episodes:
            url = f'https://www.youtube.com/watch?v={episodes[episode]["YouTube"]}'
            print(episode)
            print(url)

            htmlStr = requests.get(url).text

            htmlStr = htmlStr.split('<')

            for i in htmlStr:
                if 'RELATED_PLAYER_ARGS' in i:
                    
                    description = i.split("'RELATED_PLAYER_ARGS':")[-1]        
                    description = ''.join(description)
                    description = description.split('\\n')

                    timelineCheck = [str(i) for i in range(10)]
                    timeline = [i.rstrip('\\') for i in description if i[0] in timelineCheck] #If the line starts with str 1-9 then it's part of timeline.
                    
                    for i, stamp in enumerate(timeline):
                        if '0:00:00' in stamp:
                            startTimeline = i

                    timeline = timeline[startTimeline : ]
                    timeline[-1] = timeline[-1].split('\\"}')[0]
                    
                    finalTimeline = []
                    for i in timeline:
                        fixed = i.split('\\\\u0026')
                        fixed = '&'.join(fixed)

                        fixed = fixed.split('\\/')
                        fixed = '/'.join(fixed)
                        finalTimeline.append(fixed)

                    f.write(episode + '\n')
                    for i in finalTimeline:
                        f.write('\t' + i+'\n')
                    f.write('\n')

main('pkaInfo.json')
