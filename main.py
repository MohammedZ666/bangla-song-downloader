from bs4 import BeautifulSoup
import requests
import os
import sys
print(sys.argv)
directory = sys.argv.pop().strip()
albums = sys.argv[1:]

osposix = os.name == "posix"
if(osposix and directory[-1]!='/'):
  directory+='/'
elif(not osposix and directory[-1]!='\\'):
  directory+='\\'

for album in albums:
  album = album.strip()
  res = requests.get(album).text
  res = BeautifulSoup(res, "html.parser")

  anchs = res.find_all("a", class_="list-group-item")
  anchs.pop(0)
  songs = []
  common = album[album.index('e/')+2:]

  for  a in anchs:
    s = a.contents[2].strip()
    down = "http://download.music.com.bd/Music/" + common + s.replace(" ", "%20")
    songs.append({
        'down' : down,
        'song' : s
    })    
  songs

  for s in songs:
    res = requests.get(s['down'])
    f = open(directory + s['song'], 'wb')
    f.write(res.content)
