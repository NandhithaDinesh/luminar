import json
with open("blog.json",encoding="utf-8") as f:
    data=json.load(f)
print(data)
print(len(data))# count of posts
post=[p for p in data if p["userId"]==1]# number of post by userid=1
print(len(post))

likes=[len(p["liked_by"]) for p in data if p["postId"]==6]# total number of likes for postid 6
print(likes)

like_count=len([post for post in data if 2 in post["liked_by"] ])
print(like_count)