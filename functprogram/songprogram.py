import functools
#print total no of songs in album 1
import json
import random
with open("songs.json",encoding="utf-8") as f:
    data=json.load(f)
num_song=[song for song in data if song["album"]=="album1"]
print(len(num_song))

#print total no of songs in album 1 using filter
album_song_count=list(filter(lambda song:song["album"]=="album1",data))
print(len(album_song_count))

#highest rating song
top_song=max(data,key=lambda s:s["rating"])
print(top_song)
top_songs=[s for s in data if s["rating"]==top_song["rating"]]
print(top_songs)

#highest rating song using reduce
t_songs=functools.reduce(lambda s1,s2:s1 if s1["rating"]>s2["rating"] else s2,data)
print(t_songs)

#sad mode songs with random sample of 2
sad_songs=[s for s in data if s["mode"]=="sad"]
print(random.sample(sad_songs,2))

# total no of albums
albums=set([s["album"] for s in data])
print(len(albums))

# which album containg most songs
sc={}
for song in data:
    album_name=song.get("album")
    if album_name in sc:
        sc[album_name]+=1
    else:
        sc[album_name]=1
print(sc)
print(max(sc.items(),key=lambda s:s[1]))
