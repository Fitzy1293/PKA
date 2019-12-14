#Work can be found => https://github.com/Fitzy1293/PKA/tree/master/Audio%20Archive
#This was written on Windows with Python 3.7

#IMPORTANT TO RUN THIS PROPERLY.
    #Install the youtube-dl package however you normally install packages.
    #Download this https://ffmpeg.zeranoe.com/builds/
        #Go into the bin folder and put ffmpeg.exe in the folder where archivePKA.py is executed
        #Don't need the other stuff in the download delete all that.
        #Included a .zip on the github so you can just take it from there without all the other stuff.



#The file size of the average 4 hour PKA is ~350,000 KB.
#Assuming each is ~4 hours (the earlier ones are usually shorter)
#350,000 KB * 468 ~156 GB (Binary)

import youtube_dl
from pprint import pprint
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
    pkaUrls = getUrlsPKA()
    youtubeMP3(pkaUrls)
        
main()
