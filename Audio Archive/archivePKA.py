#VERY IMPORTANT INFO TO RUN THIS PROPERLY.
#Download this https://ffmpeg.zeranoe.com/builds/
    #Go into the bin folder and put ffmpeg.exe in the folder where archivePKA.py is executed
    #Don't need the other stuff in the download delete all that. 

import youtube_dl
from pprint import pprint
import requests
import json

def youtubeMP3(urlList):
    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
    }

    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download(urlList)

def getUrlsPKA():
    pkaJson = open('painkiller info.json', 'r').read() #Copied data from view-source:https://www.painkilleralready.info to a local .json file. 
    pkaInfo = json.loads(pkaJson)
    
    episodes = pkaInfo['episodes']
    pkaUrls = []
    for key in episodes.keys():
        pkaUrls.append('https://www.youtube.com/watch?v=' + episodes[key]['YouTube'])

    pkaUrls.reverse()
    
    return pkaUrls

def main():
    pkaUrls = getUrlsPKA()[0:1]
    youtubeMP3(pkaUrls)
        
main()
