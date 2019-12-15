import requests
import os
from pprint import pprint
import json
import csv

#painkilleralready.info didn't have all timelines available.
#Youtube has an api but didn't feel like learning it.
def writeTimelines():
    f = open('pkaInfo.json', 'r') 
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
                        if stamp[0].isnumeric() and stamp[1]==':' and stamp[2:4].isnumeric():
                            lastStart.append(i)
                            hasTimelineFlag = True
                            break
       
                    if hasTimelineFlag:
                        timeline[-1] = timeline[-1].split('"}')[0]
                        
                        finalTimeline = []
                        for j in timeline[lastStart[-1]:]:
                            fixed = j.split('\\\\u0026')
                            fixed = '&'.join(fixed)
                            fixed = fixed.split('\\')
                            fixed = ''.join(fixed)
                            finalTimeline.append(fixed)

                        f.write(episode + ' - ' + url + '\n')
                        for j in finalTimeline:
                            if 'allowRatings' in j:
                                f.write('\t' + j.split('"')[0] + '\n')
                                break

                            f.write('\t' + j +'\n')
                                
                        f.write('\n')

                    else:
                        f.write(episode + ' - ' + url + '\n\n')
                
writeTimelines()
