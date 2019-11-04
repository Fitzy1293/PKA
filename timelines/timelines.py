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

    with open('Timeline.txt','w+',encoding='utf-8') as f:
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

                    hasTimelineFlag= False
                    lastStart = []
                    for i, stamp in enumerate(timeline):
                        #pprint(stamp)
                        if stamp[0:6] == '0:00:0': #Some timelines do not start at 0
                            lastStart.append(i)
                            hasTimelineFlag = True
                        if stamp[0:5] == '0:00 ': #Some timelines started with a minute and second level accuracy
                            lastStart.append(i)
                            hasTimelineFlag = True
                            break

                    if hasTimelineFlag:
                        timeline[-1] = timeline[-1].split('\\"}')[0]
                        
                        finalTimeline = []
                        for i in timeline[lastStart[-1]:]:
                            fixed = i.split('\\\\u0026')
                            fixed = '&'.join(fixed)

                            fixed = fixed.split('\\')
                            fixed = ''.join(fixed)
                            finalTimeline.append(fixed)

                        f.write(episode + ' - ' + url + '\n')
                        for i in finalTimeline:
                            f.write('\t' + i+'\n')
                        f.write('\n')

                    else:
                        f.write(episode + ' - ' + url + '\n\n')
                
main('pkaInfo.json')
