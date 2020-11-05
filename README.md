# PKA

Concatenate LegitimateRage's descriptions into one file. \
[This playlist](https://www.youtube.com/playlist?list=PL568FBE856C240972) had the most complete list of PKA urls.

[Here's the link to that file](https://github.com/Fitzy1293/PKA/blob/master/PKA_timelines.txt?raw=true)


![How each episode looks](https://i.imgur.com/A39tlQM.png)


To get the descriptions I used yt-dl (R.I.P their github page) with the command

`youtube-dl "$(cat playlist-url)" --write-info-json --skip-download -i`

Some were still not in that playlist so I ran this with the missing episode's URL as the argument.

`cd json && youtube-dl "$1" --write-info-json --skip-download -i && cd ..`


The code mostly deals with finding the episode number from the json file names to sort.  
