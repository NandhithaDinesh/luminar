import json
import random
try:
    with open("../blog/users.json") as f:
        data=json.load(f)
        print(data)

        all_users=[user["id"] for user in data ]
        my_followings=[user["followers"] for user in data if user["username"]=="akhil" ][0]
        my_id=[user["id"] for user in data if user["username"]=="akhil"].pop()
        to_follow=set(all_users)-set(my_followings)
        to_follow.remove(my_id)
        print(to_follow)
        suggessions=random.sample(to_follow,2)
        print(suggessions)
except Exception as e:
    print(e.__class__)

# destructuring of set to list
st={23,9,8,1,0}
lst=[*st]
print(lst)

# destructuring of list to set
lst=[23,9,8,1,0]
st={*st}
print(st)