#This program is for searching PKA's topics.
#Enter one word, and it will search all of the info available through www.painkilleralready.com's API.
#Search time is a little long, around 120 seconds. It is searching through every word individually though. 

import requests
import json
from pprint import pprint
import re
import time

def main():
    searchTerm = input('Enter a word to search for in PKA topics >> ')
    print('This may take some time.')

    start = time.time()
    jsonTemplate = 'https://www.painkilleralready.com/api/episode.php?episode=' #Adding episode number on the end
                                                                                #Gives json data for that episode.
    aggregateMatches = []
    for i in range(1,428): #Current PKA is 427. 
        episodeSearch = searchTopics(searchTerm, getEpisodeInfo(jsonTemplate + str(i)))
        if len(episodeSearch) != 0:
            aggregateMatches.append(episodeSearch)

    end = time.time()
    
    for episode in aggregateMatches: #Final printout.    
        for match in episode:  
            print('PKA episode ' + str(match[0]) + '.')
            print(match[1][0])
            print(' '.join(match[1][1]))
            print()
   
    print('Search time: ' + str(end - start) + ' seconds.')

def getEpisodeInfo(url):
    try:
        episode = json.loads(requests.get(url).text) #Dictionary of loaded json data.
    
        episodeInfo = [] #List containing the episode number
                         #And a tuple containing the timestamp and a list of each word in that timestamps 'Value'.
        episodeInfo.append(episode['Number'])

        if episode['Timelined'] != 'false':
            for topic in episode['Timeline']['Timestamps']: #episode['Timeline']['Timestamps'] is where to find topic info. 
                episodeInfo.append((topic['HMS'], topic['Value'].split(' ')))

        return episodeInfo

    except ValueError:
        print('Could not load episode ' + url.split('=')[-1] + '\'s info.')
        return []

def searchTopics(searchTerm, episodeInfo): 
    topicMatch = []
    for topic in episodeInfo[1:]:
        for word in topic[1]:
            if searchTerm.lower() == re.sub('[^A-Za-z0-9]+', '', word).lower(): #Gets rid of non alpha-num characters. 
                topicMatch.append((episodeInfo[0],topic))

    return topicMatch

main()
