# #number of movies released in 2022
# fread=open("movies.txt","r")
# all_movies=[movie.rstrip("\n").split(",") for movie in fread]
# movie22=[movie for movie in all_movies if movie[1]=="2022"]
# print(f"number of movies relesed in 2022 are {len(movie22)} and they are {movie22}")
#
# #number of malayalam movies
# fread=open("movies.txt","r")
# all_movies=[movie.rstrip("\n").split(",") for movie in fread]
# malayalam=[movie for movie in all_movies if movie[3]=="malayalam"]
# print(f"number of malayalam movies are {len(malayalam)} and they are {malayalam}")
#
# #theater released movies
# fread=open("movies.txt","r")
# all_movies=[movie.rstrip("\n").split(",") for movie in fread]
# theater=[movie for movie in all_movies if movie[-1]=="theater"]
# print(f"number of theater released movies are {len(theater)} and they are {theater}")
#
# #ist of movies whose rating >5
# fread=open("movies.txt","r")
# all_movies=[movie.rstrip("\n").split(",") for movie in fread]
# rating=[movie for movie in all_movies if movie[2]>"5"]
# print(f"number of movies whose rating greater than 5 are {len(rating)} and they are {rating}")


fread=open("movies.txt","r")
all_movies=[movie.rstrip("\n").split(",") for movie in fread]
movie_out={}
for movie in all_movies:
    year=movie[1]
    if year in movie_out:
        movie_out[year]+=1
    else:
        movie_out[year]=1
print(movie_out)
print(movie_out.items())
out=max(movie_out.items(),key=lambda item:item[1])
print(out)
